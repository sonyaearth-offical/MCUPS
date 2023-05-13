import json
import os
import shutil
import datetime
from cleo.commands.command import Command
from cleo.helpers import argument, option

class Backup(Command):
    name = "create"
    description = "Create Backup"

    arguments = [
        argument(
            "config_number",
            description="locale on backup config number.",
            optional=False
        )
    ]

    def handle(self):
        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        now = datetime.datetime.now(JST)
        d = now.strftime('%Y-%m-%d_%H-%M_%S')

        num = int(self.argument("config_number"))

        with open(os.getenv('BACKPAK_CONFIG'), "r", encoding="utf-8") as f:
            l = json.load(f)
            ignore = l["main"][num]["path"]["ignore"]
            src_dir = l["main"][num]["path"]["src"]
            dst_dir = os.path.join(l["main"][num]["path"]["output"], d)

            shutil.copytree(src_dir, dst_dir, ignore=shutil.ignore_patterns(*ignore))

class BackUp():
    @staticmethod
    def create(num):
        with open(os.getenv('BACKPAK_CONFIG'), "r", encoding="utf-8") as f:
            l = json.load(f)
            ignore = l["main"][num]["path"]["ignore"]
            src_dir = l["main"][num]["path"]["src"]
            dst_dir = l["main"][num]["path"]["output"]

            shutil.copytree(src_dir, dst_dir, ignore=shutil.ignore_patterns(*ignore))