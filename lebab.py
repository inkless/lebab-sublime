# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sublime, sublime_plugin
import platform
import os, sys
from subprocess import Popen, PIPE

PROJECT_NAME = "lebab"
SETTINGS_FILE = PROJECT_NAME + ".sublime-settings"

IS_WINDOWS = platform.system() == 'Windows'


class LebabCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            node_path = get_node_path()
            lebab_path = get_lebab_path()

            if lebab_path is False:
                sublime.error_message('Lebab could not be found on your path')
                return

            # TODO
            # convert code when not saved
            if not self.view.file_name():
                sublime.error_message('Please save the file before run lebab')
                return

            transforms = get_transforms()

            cmd = [node_path, lebab_path, '-t', ','.join(transforms), self.view.file_name(), '-o', self.view.file_name()]

            cdir = os.path.dirname(self.view.file_name())

            execute(cmd, cdir)

        except:
            # Something bad happened.
            msg = str(sys.exc_info()[1])
            print("Unexpected error({0}): {1}".format(sys.exc_info()[0], msg))
            sublime.error_message(msg)


def get_pref(key):
    global_settings = sublime.load_settings(SETTINGS_FILE)
    value = global_settings.get(key)

    # Load active project settings
    project_settings = sublime.active_window().active_view().settings()

    # Overwrite global config value if it's defined
    if project_settings.has(PROJECT_NAME):
        value = project_settings.get(PROJECT_NAME).get(key, value)

    return value


def get_node_path():
    platform = sublime.platform()
    node = get_pref("node_path").get(platform)
    print("Using node.js path on '" + platform + "': " + node)
    return node


def get_lebab_path():
    platform = sublime.platform()
    lebab = get_pref("lebab_path").get(platform)
    print("Using lebab path on '" + platform + "': " + lebab)
    return lebab


def get_transforms():
    transforms = get_pref("transforms")
    print("Transforms option " + str(transforms))
    return transforms


def execute(cmd, cdir):
    try:
        p = Popen(cmd,
                  stdout=PIPE, stdin=PIPE, stderr=PIPE,
                  cwd=cdir, shell=IS_WINDOWS)
    except OSError:
        raise Exception('Couldn\'t find Node.js. Make sure it\'s in your $PATH by running `node -v` in your command-line.')
    stdout, stderr = p.communicate()
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')

    if stderr:
        raise Exception('Error: %s' % stderr)
    else:
        return stdout
