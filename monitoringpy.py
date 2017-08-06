# monitoringpy

"""
File monitoring script. It will monitor given folder and run external script
"""

import os
import time
from datetime import datetime
import subprocess

monitoring_folder = "C:\\projects\\wsw\\" # monitioring folder path
monitoring_files = "main.ui" # specify files for monitoring

if not monitoring_folder:
    monitoring_folder = os.getcwd()
if not monitoring_files:
    monitoring_files = os.listdir()

def monitoring():

    folder = os.listdir(monitoring_folder)

    files_old = {}
    files_new = {}

    for file in folder:
        if file in monitoring_files:
            files_old[file] = os.stat(monitoring_folder + file).st_mtime


    time.sleep(10)
    for file in folder:
        if file in monitoring_files:
            files_new[file] = os.stat(monitoring_folder + file).st_mtime

    for key in files_old:
        for key2 in files_new:
            if files_old[key] != files_new[key2]:
                # external script path and command
                subprocess.call("pyuic5 -x " + monitoring_folder + "main.ui -o " + monitoring_folder + "main.py")

                print("FILE GENERATED", key2, datetime.now().time())
                files_new = files_old

while True:
    monitoring()
