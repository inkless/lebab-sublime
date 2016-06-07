Lebab for Sublime Text 3
========================
A plugin to convert ES5 code to ES6 code.

##Installation
####Prerequisites
The plugin requires an npm module `lebab` installed in you machine locally.

1. Install [Node.js](https://nodejs.org)
2. Install [lebab](http://lebab.io/)
```bash
npm install -g lebab
```

####Install plugin
Please use [Package Control](https://sublime.wbond.net/installation) to install the plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.
2. When the plugin list appears, type `lebab`. Among the entries you should see `Lebab`. If that entry is not highlighted, use the keyboard or mouse to select it.

####Install manually (Optional)
Download this repository to your sublime's package:

**Windows:**
```
%APPDATA%\Sublime Text 3\Packages
```

**OS X:**
```
~/Library/Application Support/Sublime Text 3/Packages
```

**Linux:**
```
~/.config/sublime-text-3/packages
```

## Commands
**Command palette:**

- Lebab: convert ES5 to ES6

**Shortcut key:**

* Linux/Windows: [Ctrl + Shift + L]
* Mac: [Cmd + Shift + L]

## Contributing

If you find any bugs feel free to report them [here](https://github.com/inkless/lebab-sublime/issues).

Pull requests are also encouraged.