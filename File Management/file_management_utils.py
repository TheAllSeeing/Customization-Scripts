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
    return ['/home/atai/' + path for path in os.listdir(escape(var(at))) if path.startswith('Code')]

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

