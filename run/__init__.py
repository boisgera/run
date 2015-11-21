#!/usr/bin/env python

# Future
from __future__ import print_function

# Python 2.7 Standard Library
import os
import sys

# Third-Party Libraries
from pathlib import Path
import sh

# ------------------------------------------------------------------------------

## open local ./run.js / ./run.coffee / .run.py ? to get some json ?
## ATM, hardcode "boisgera/pandoc"

def main():
    image = "boisgera/pandoc"

    # Register the current user and commit the image
    username = os.environ["USER"]
    userid = str(sh.id("-u", username)).strip()
    cmd = ["useradd", "-u", userid, username]

    sh.docker.run(image, cmd)
    container_id = str(sh.docker.ps("-ql")).strip()
    image = str(sh.docker.commit(container_id)).strip()


    # Execute the command.
    cmd = " ".join(sys.argv[1:]) or "true"
    mount = ["-v", "{cwd}:/tmp".format(cwd=Path.cwd())]
    as_user = ["-u", username]
    bash = "/bin/bash -c".split()
    cmd = "cd /tmp && " + cmd
    for line in sh.docker.run(mount, as_user, image, bash, cmd, _iter=True):
      print(line, end="")


