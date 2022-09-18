#!/usr/bin/python3

import subprocess
import re

def executeCommand(command, expectedOutput):
    commandOutput = ""
    try:
        commandOutput = (subprocess.check_output(command, shell = True, timeout=10, stderr = subprocess.STDOUT)).decode()
    except subprocess.TimeoutExpired:
        print("Timeout Exception")
    finally:
        pattern = re.compile(expectedOutput, re.MULTILINE)
        if(pattern.search(commandOutput) != None):
            print("Success: Matched expected string.")
        else:
            print("Failed: Missing expected string {}".format(expectedOutput))
        print("======================================================")
        print(commandOutput)
        print("======================================================")


executeCommand("ls -l", r"sleep\d+.py")
executeCommand("ls -l", r"sleep\w+.py")

