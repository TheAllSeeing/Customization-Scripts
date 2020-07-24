import subprocess as sp
import os

def escape(string: str):
    string = string.replace(' ', '\ ')
    string = string.replace('(', '\(')
    string = string.replace(')', '\)')
    string = string.replace('&', '\&')
    return string

projs = sp.check_output('find ~ -maxdepth 4 -type d -name "*.proj"', shell=True)
projs = [escape(path) for path in str(projs)[2:].split('\\n')[:-1]]
names = [path.split('/')[-1] for path in projs]

os.chdir('/home/atai/Projects')
[os.system('ln -s ' + path + ' ' + os.getcwd() + '/' + name) for path, name in zip(projs, names)]
