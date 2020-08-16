import subprocess as sp
import os
import re

def var(name):
    return os.environ[name]

def get_dossier_paths(extension='*', at: str='HOME', code: int=0, path_type: int=0) -> list: 
    # code_0 - ongoing dossiers (main)
    # code_1 - archive and hold dossiers
    # code_2 - held dossiers
    # code_3 - ongoing dossiers' archive
    # code_4 - archived, complete dossiers.

    # path_type_0 - path
    # path_type_1 - filename
    # path_type_2 - name
    # path_type_3 - aspect

    if path_type == 1:
        return [path.split('/')[-1] for path in get_dossier_paths(extension, at, code, 0)]
    if path_type == 2:
        return [file[:-4] for file in get_dossier_paths(extension, at, code, 1)]
    if path_type == 3:
        return [path.split('/')[-2] for path in get_dossier_paths(extension, at, code, 0)]
        
    
    working_directory = escape(var(at))
    if  0 < code <= 4:
            working_directory += '/' + escape(var('ARCHIVES'))
            
    res = find(options=working_directory + '/Code* -maxdepth 1 -name "*.' + extension + '"')
    if code == 2:
        return [path for path in res if path.split('|')[0].endswith('-')]
    if code == 3:
        return [path for path in res if path.split('|')[0].endswith('+')]
    if code == 4:
        return [path for path in res if not path.split('|')[0].endswith('-') and not path.split('|')[0].endswith('+')]
    return res



def get_aspect_paths(at='HOME', archive=False):
    working_directory = escape(var(at))
    if archive:
            working_directory += '/' + escape(var('ARCHIVES'))
    return find(options=working_directory + ' -maxdepth 1 -name "Code-*(*)"')

def get_aspect_filenames(at='HOME'):
    return [path.split('/')[3] for path in get_aspect_paths(at)]

def get_aspect_codes(at='HOME'):
    return [name.split('(')[1][:-1] for name in get_aspect_filenames(at)]

def get_aspect_colors(at='HOME'):
    return [name.split(' (')[0].split('-')[1] for name in get_aspect_filenames(at)]

def path_of_dossier(dossier_name):
    return get_dossier_paths()[get_dossier_names().index(dossier_name)]

def get_archive_start(archived_dossier):
    return archived_dossier.split('/')[-1].split('|')[0].split('-')[0][:4]

def get_archive_end(archived_dossier):
    if archived_dossier.split('|')[0][-1] == '+':
            return -1
    if archived_dossier.split('|')[0][-1] == '-': # if frozen return freezing yeat
            return archived_dossier.split('/')[-1].split('|')[0].split('-')[-2][:4]
    return archived_dossier.split('/')[-1].split('|')[0].split('-')[-1][:4]

def escape(path):
    return path.replace(' ', '\ ').replace('&', '\&').replace('(','\(').replace(')', '\)').replace('|', '\|')

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

