import sublime_plugin

class OpenInGitBashCommand(sublime_plugin.WindowCommand):
    def run(self, **args):
        dir = ""+args["dirs"][0]+""
        self.window.run_command("exec", {"shell_cmd": "start cmd /k \"\"C:\\Program Files (x86)\\Git\\bin\\sh.exe\" --login -i\"", "shell": True, "working_dir": dir})
        self.window.run_command("hide_panel", {"panel": "output.exec"})

    def is_visible(self, **args):
        return len(args["dirs"]) > 0
