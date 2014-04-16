#!/usr/bin/env python

from distutils.core import setup
import subprocess
import sys
import os

path = os.path.dirname(os.path.realpath(__file__))

submodule_path = os.path.join(path, "spacescout_web")

subprocess.call(["git", "submodule", "init"], cwd=path)
subprocess.call(["git", "submodule", "update"], cwd=path)
subprocess.call(["git", "submodule", "foreach", "git", "pull", "origin", "master"], cwd=path)

setup(name='SpaceScout-Web-Wrapper',
      version='1.0',
)

subprocess.call(["pip", "install", "-r", "base-requirements.txt"], cwd=submodule_path)
