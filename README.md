# Compile Selected ES6 Package for Sublime Text 3

## [DEPRECATED] This project has been deprecated – please use the official project [babel-sublime](https://github.com/babel/babel-sublime) instead

A sublime plugin for compiling the selected es6 code on the fly, since the babel sublime plugin did not provide this feature


## Requirements

In order for build system to work you will need [babel](https://babeljs.io/) installed via [npm](http://nodejs.org/) and available in your `PATH`.

## Install

The easiest way to install this is with [Package Control](https://sublime.wbond.net/).

 * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Select **Compile Selected ES6** when the list appears.

Package Control will automatically keep the package up to date with the latest version.

## Screenshots

![the-usage-of-plugin](https://raw.githubusercontent.com/xinchaobeta/compile-selected-es6/master/screenshots/usage.png)

* `Compile Select ES6` plugin supports both javascript ES6 sytax and JSX syntax. First you select the content you want to compile, then you right click the mouse and select `compile es` menu.

![the-result-of-compiled-code](https://raw.githubusercontent.com/xinchaobeta/compile-selected-es6/master/screenshots/result.png)

* Now you got the compiled code.

>  Note that you can also use the keyboard shortcut `Option+Shift+d` to compile the code without using the mouse way.


----------


![check-syntax-on-save](https://raw.githubusercontent.com/xinchaobeta/compile-selected-es6/master/screenshots/check-onsave.png)

* By default, the plugin will check synax error when you save the file. You can disable this feature by changing the plugin user setting `checkSyntaxOnSave` to false.



## Settings

Go to `Preferences > Package Settings > Compile Selected ES6 > Settings - User` to change settings.

Full details in the comments in `Preferences > Package Settings > Compile Selected ES6 > Settings - Default`

There's two ways to change [the `stage` option](http://babeljs.io/docs/usage/options/#options). One way is using the
plugin user setting. Another way is [creating a `.babelrc` file in the project directory](https://babeljs.io/docs/usage/babelrc/). The `.babelrc` file settings will override the plugin user settings.

> Note if you changed the `stage` value in the settings, make sure you installed the latest version of Babel whose CLI support  `--stage` . 

## Issues & Feature Requests

Please use [GitHub Issue Tracker](https://github.com/xinchaobeta/compile-selected-es6/issues) to report any bugs and make feature requests.

## Licensing
Licensed under permissive MIT-style license
