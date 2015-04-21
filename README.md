# Compile Selected ES6 Package for Sublime Text 3

A sublime plugin for compiling the selected es6 code on the fly, since the babel sublime plugin did not provide this feature


## Requirements

In order for build system to work you will need [babel](https://babeljs.io/) installed via [npm](http://nodejs.org/) and available in your `PATH`.

## Install

The easiest way to install this is with [Package Control](https://sublime.wbond.net/).

 * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Select **Compile Selected ES6** when the list appears.

Package Control will automatically keep the package up to date with the latest version.

# Settings

Go to `Preferences > Package Settings > Compile Selected ES6 > Settings - User` to change settings.

You can set paths to the stylus binary, and other plugin settings including `compileOnSave` which is off by default, `compress` and output paths.

Full details in the comments in `Preferences > Package Settings > Compile Selected ES6 > Settings - Default`


## Issues & Feature Requests

Please use [GitHub Issue Tracker](https://github.com/xinchaobeta/compile-selected-es6/issues) to report any bugs and make feature requests.

## Licensing
Licensed under permissive MIT-style license