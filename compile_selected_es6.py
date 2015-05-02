from subprocess import Popen, PIPE
import sublime, sublime_plugin, os

def isJSX(view=None):
    if view is None:
        view = sublime.active_window().active_view()
    return 'source.js' in view.scope_name(0)

def settings_get(name, default=None):
    # load up the plugin settings
    plugin_settings = sublime.load_settings('compile_selected_es6.sublime-settings')
    return plugin_settings.get(name, default) or default   

def compile(source=''):
  env = {
    'PATH': settings_get('envPATH', os.environ.get('PATH'))
  }
  stage = settings_get('stage', '2')
  # lagency babel did not support --stage arguments
  # so if a user modified default stage, then i can sure he installed the lastest version  
  if stage is not 2:
    command = ['babel', '--stage', stage]
  else:
    command = ['babel']

  proc = Popen(command, env=env, cwd=None, stdout=PIPE, stdin=PIPE, stderr=PIPE)
  stat = proc.communicate(input=source.encode('utf-8'))
  return {"okay": proc.returncode == 0, "out": stat[0].decode('utf-8'), "err": stat[1].decode('utf-8')}

class Text():
  @staticmethod
  def all(view):
    return view.substr(sublime.Region(0, view.size()))

  @staticmethod
  def sel(view):
    text = []
    for region in view.sel():
      if region.empty():
        continue
      text.append(view.substr(region))
    return "".join(text)

  @staticmethod
  def get(view):
    text = Text.sel(view)
    if len(text) > 0:
      return text
    return Text.all(view)

class CompileSelectedEs6Command(sublime_plugin.TextCommand):
  def is_enabled(self):
      return isJSX(self.view)
  def run(self, edit):
    output = self.view.window().new_file()
    output.set_scratch(True)
    output.set_syntax_file('Packages/JavaScript/JavaScript.tmLanguage')
    res = compile(Text.get(self.view))    
    if res["okay"] is True:
        output.insert(edit, 0, res["out"])
    else:
        output.insert(edit, 0, res["err"])

