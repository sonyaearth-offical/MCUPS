#!/usr/bin/env python

from mcups.cli.backup import Backup
from mcups.cli.envlib import getenv
from cleo.application import Application

def main():
    application = Application()
    application.add(Backup())
    application.add(getenv())
    application.run()