from cleo.commands.command import Command
from cleo.helpers import argument, option
import os

class getenv(Command):
    name = "env"
    description = "show env"
    arguments = [
        argument(
            "env",
            description="env name",
            optional=False
        )
    ]

    def handle(self):
        env = self.argument("env")
        if os.getenv(env) is not None:
            print("---------------------------")
            print(f"\n{env}: " + os.getenv(env))
            print("---------------------------")
        elif os.getenv(env) is None:
            print("---------------------------")
            print(f"\n{env}does not exist.")
            print("---------------------------")