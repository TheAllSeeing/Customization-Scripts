import subprocess as sp
import os
import re

def get_project_paths():
    return ['/' + path for path in str(sp.check_output('echo ~/Code*/*.prj', shell=True)).split(' /')[3:-3]]

def get_project_filenames():
    return [path.split('/')[4] for path in get_project_paths()]

def get_project_names():
    return [file[:-4] for file in get_project_filenames()]

def get_routine_paths():
    return ['/' + path for path in str(sp.check_output('echo ~/Code*/*.prj', shell=True)).split(' /')[3:-3]]

def get_routine_files():
    return [path.split('/')[4] for path in  get_routine_paths]

def get_routine_names():
    return [file[:-4] for file in get_routine_filenames()]

def get_dossier_paths():
    return sorted(get_project_paths() + get_routine_paths())


def get_dossier_filenames():
    return [path.split('/')[4] for path in get_dossier_paths()]

def get_dossier_names():
    return [file[:-4] for file in get_dossier_filenames()]

def get_aspect_paths():
    return ['/home/atai/' + path for path in os.listdir('/home/atai') if path.startswith('Code')]

def get_aspect_filenames():
    return [path.split('/')[3] for path in get_aspect_paths()]

def get_aspect_codes():
    return [name.split('(')[1][:-1] for name in get_aspect_filenames()]

def get_aspect_colors():
    return [name.split(' (')[0].split('-')[1] for name in get_aspect_filenames()]

def path_of_dossier(dossier_name):
    return get_dossier_paths()[get_dossier_names().index(dossier_name)]

def escape(path):
    return path.replace(' ', '\ ').replace('&', '\&').replace('(','\(').replace(')', '\)')

