import subprocess as sp
import os
import re

def var(name):
    return os.environ[name]

def get_project_paths(at='HOME'):
    return ['/' + path for path in str(sp.check_output('echo ' + escape(var(at)) + '/Code*/*.prj', shell=True))[3:-3].split(' /')]

def get_project_filenames(at='HOME'):
    index = 4
    if at == 'DRIVE':
        index = 7
    if at == 'PHONE':
        index = 9
    return [path.split('/')[index] for path in get_project_paths(at)]

def get_project_names(at='HOME'):
    return [file[:-4] for file in get_project_filenames(at)]

def get_routine_paths(at='HOME'):
    return ['/' + path for path in str(sp.check_output('echo ' + escape(var(at)) + '/Code*/*.rou', shell=True))[3:-3].split(' /')]

def get_routine_filenames(at='HOME'):
    return [path.split('/')[4] for path in  get_routine_paths(at)]

def get_routine_names(at='HOME'):
    return [file[:-4] for file in get_routine_filenames(at)]

def get_dossier_paths(at='HOME'):
    return sorted(get_project_paths(at) + get_routine_paths(at))


def get_dossier_filenames(at='HOME'):
    return [path.split('/')[4] for path in get_dossier_paths(at)]

def get_dossier_names(at='HOME'):
    return [file[:-4] for file in get_dossier_filenames(at)]

def get_aspect_paths(at='HOME'):
    working_directory = escape(var(at))
    return find(options=working_directory + ' -maxdepth 1 -name "Code-*(*)"')

def get_aspect_filenames(at='HOME'):
    return [path.split('/')[3] for path in get_aspect_paths(at)]

def get_aspect_codes(at='HOME'):
    return [name.split('(')[1][:-1] for name in get_aspect_filenames(at)]

def get_aspect_colors(at='HOME'):
    return [name.split(' (')[0].split('-')[1] for name in get_aspect_filenames(at)]

def path_of_dossier(dossier_name):
    return get_dossier_paths()[get_dossier_names().index(dossier_name)]

def escape(path):
    return path.replace(' ', '\ ').replace('&', '\&').replace('(','\(').replace(')', '\)')

def _wrap_command_with_output(command: str, default_options='', seperator=None) -> callable:
    def res(options=default_options, sudo=False):
        _command = command
        if sudo:
            _command = 'pkexec ' + _command
        _command += ' ' + options
        output = str(sp.check_output(_command, shell=True))[2:-3]
        if seperator != None:
            return  output.split(seperator)
        return output

    return res

def _wrap_run_with_one_parameter(command: str, default_options='') -> callable:
    def res(targets, options=default_options, sudo=False):
        _command = command
        if sudo:
            _command = 'pkexec ' + command
        _command += ' ' + options
        if type(targets) == str:
            return os.system(_command + ' ' + targets)
        else:
            return [res(target, options, sudo) for target in targets]
            
    return res

def _wrap_run_with_two_parameters(command: str, default_options: str='') -> callable:
    def res(targets, destinations, options=default_options, sudo=False):
        _command = command
        if sudo:
            _command = 'pkexec ' + command
        _command += ' ' + options
        if type(targets) == str:
            return os.system(_command + ' ' + targets + ' ' + destinations)
        else:
            return [res(target, dest, options, sudo) for target, dest in zip(targets, destinations)]
    return res

mkdir = _wrap_run_with_one_parameter('mkdir')
remove = _wrap_run_with_one_parameter('rm')
trash = _wrap_run_with_one_parameter('rmtrash')
touch = _wrap_run_with_one_parameter('touch')
symlink = _wrap_run_with_two_parameters('ln -s')
hardlink = _wrap_run_with_two_parameters('ln')
move = _wrap_run_with_two_parameters('mv')
copy = _wrap_run_with_two_parameters('cp')
find = _wrap_command_with_output('find', seperator='\\n')
ls = _wrap_command_with_output('ls', seperator='\\n')
exa = _wrap_command_with_output('exa', seperator='\\n')

