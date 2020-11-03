#!/usr/bin/env python
from setuptools import setup, find_packages
from subprocess import Popen, PIPE

Version = "8.2.1"
p = Popen(
    ("git",
     "describe",
     "--tags"),
    stdin=PIPE,
    stdout=PIPE,
    stderr=PIPE)
try:
    descr = p.stdout.readlines()[0].strip().decode("utf-8")
    Version = "-".join(descr.split("-")[:-2])
    if Version == "":
        Version = descr
except:
    descr = Version


setup (name = "WK",
       version=descr,
       description = "Package to compute and draw the Wheeler-Kiladis figures",
       url = "http://cdat.sf.net, see WK 99",
       packages = find_packages(),
       data_files = [("share/wk",["share/test_data_files.txt"])],
      )
