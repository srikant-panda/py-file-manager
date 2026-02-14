import os
import shutil


def pwd():
    return os.getcwd()

def cd(filepath):
    os.chdir(filepath)
    return os.getcwd()

def ls(filepath):
    return os.listdir(filepath)

def create(filepath):
    os.mkdir(filepath)

def delete(filepath):
    os.rmdir(filepath)

def copyfile(src,dst):
    shutil.copy2(src,dst)
def copydir(src,dst):
    shutil.copytree(src,dst)
