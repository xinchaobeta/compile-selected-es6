from subprocess import Popen, PIPE
import sublime, sublime_plugin, os, json

def readBabelrc():
  try:
    variables = sublime.active_window().extract_variables()
    if "folder" in variables :
      path = variables["folder"] + '/.babelrc'
    elif "file_path" in variables :
      path = variables["file_path"] + '/.babelrc'
    with open(path) as babelrc :
      config = json.load(babelrc)
  except:
    config = {}
  return config

def isJSX(view=None):
    if view is None:
        view = sublime.active_window().active_view()
    scope_name_arr = view.scope_name(0).split()
    return 'source.js' in scope_name_arr or 'source.js.jsx' in scope_name_arr

def settings_get(name, default=None):
    # load up the plugin settings
    plugin_settings = sublime.load_settings('compile_selected_es6.sublime-settings')
    return plugin_settings.get(name, default) or default   

def compile(source=''):
  env = {
    'PATH': settings_get('envPATH', os.environ.get('PATH'))
  }
  babelrc = readBabelrc()
  stage = str(settings_get('stage', '2'))
  if "stage" in babelrc :
    stage = str(babelrc["stage"])
  # lagency babel did not support --stage arguments
  # so if a user modified default stage, then i can sure he installed the lastest version  
  if stage is not "2":
    command = ['babel', '--stage', stage]
  else:
    command = ['babel']

  proc = Popen(command, env=env, cwd=None, stdout=PIPE, stdin=PIPE, stderr=PIPE)
  stat = proc.communicate(input=source.encode('utf-8'))
  return {"okay": proc.returncode == 0, "out": stat[0].decode('utf-8'), "err": stat[1].decode('utf-8')}

def extractError(str=''):
  str = '\n'.join(str.split("\n")[4:])
  return str.split('    at ')[0]

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
    print('hello world')
    output = self.view.window().new_file()
    output.set_scratch(True)
    output.set_syntax_file('Packages/JavaScript/JavaScript.tmLanguage')
    res = compile(Text.get(self.view))    
    if res["okay"] is True:
        output.insert(edit, 0, res["out"])
    else:
        output.insert(edit, 0, res["err"])

class CaptureEditing(sublime_plugin.EventListener):

  def is_enabled(self, view):
      return isJSX(view)

  def on_post_save(self, view):
      if not self.is_enabled(view):
          return
      if settings_get("checkSyntaxOnSave", False):
          res = compile(Text.get(view))
          if res["okay"] is True:
              sublime.status_message("Syntax is valid.")
          else:
              sublime.message_dialog('Syntax error: %s' % extractError(res["err"]))


