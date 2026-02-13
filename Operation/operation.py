import os

# Navigation
# default_path= '/home/s-fedora/'
# default_symbol = '~$' 

def cd(filepath):
    os.chdir(filepath)
    return os.getcwd()
def ls():
    return os.listdir(os.getcwd())