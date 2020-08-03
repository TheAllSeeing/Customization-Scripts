import subprocess as sp
import os

def get_projects():
    return ['/' + path for path in str(sp.check_result('echo ~/Code*/*.prj', shell=True))[3:-3]]

def get_routines():
    return ['/' + path for path in str(sp.check_result('echo ~/Code*/*.prj', shell=True))[3:-3]]
