#%%
import os
import getpass

#%%
#getting the loggedin user name
print(getpass.getuser())

#%%
#get current working directory
print(os.getcwd())

#%%

#change directory

os.chdir(r'E:\Pycharm_Workspace\Data_Science')
print(os.getcwd())

# os.chdir(r'models')
# print(os.getcwd())

#%%
#list all folders or directories or file name
print(os.listdir())

#%%

#if you need to create a single level directory
os.mkdir(r'sysmodule')

#%%
#if you need to create multilevel directory use makedirs
# you can make single level directory with makedirs

os.makedirs('sysmodule/sysmodule')

#%%
# if you need to remove a dir for a single level -- rmdir
os.rmdir('sysmodule2/iris.data')

#%%
# to remove a file use os.remove()
os.remove('sysmodule2/winter.csv')

#%%
# if you need to remove a dir for multiple level -- removedirs
# if inside sysmodule only __init__.py is there then both sysmodule and __init__.py will be removed
# if inside sysmodule if apart from __init__.py any other module exist then only __init__.py will be removed using below command

os.removedirs('sysmodule/__init__.py')

#%%
''' Suppose you have a multilevel directory as below
   | sysmodule
       | system
           | lenovo
           | sholay
       | data_science
       | django
 if you want to remove the complete tree use shutil
 
 import shutil
 shutil.rmtree('/folder_name')
 
 # this will ignore the read-only files but in case you want to delete read_only files as well use
 shutil.rmtree('/folder-name', ignore_errors=True)
'''

import shutil
shutil.rmtree(r'sysmoudle')

#%%

# if you want to rename a directory or a file use: os.rename(original_filename, new_filename)
os.rename('sysmoudle-2','sysmodule2')

#%%
# if you want to see the stats of a file or a directory

print(os.stat('sysmodule2'))

#get size of a directory or a file
print(os.stat('sysmodule2/winter.csv').st_size)

# get mtime of a directory
mtime = os.stat(r'sysmodule2/winter.csv').st_mtime

#to convert mtime to human readable format
from datetime import datetime
print(datetime.fromtimestamp(mtime))

#%%
'''
os.walk(top, topdown=True, onerror=None, followlinks=False)
Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the 
tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
'''

for dirpath, dirname, filename in os.walk(os.getcwd()):
    print('Current Path: ', dirpath)
    print('Directories: ', dirname)
    print('Files: ', filename)
    print('==============================')

#%%
'''
get environ variables
'''

print(os.environ.get('Path'))

# list all the environment
print(os.environ)

#%%

'''
os.path.join()
for joining two file paths together
'''

create_path = os.path.join(os.environ.get('Path').split(';')[0], 'sanket.txt')
print(create_path)

#%%
'''
to get the dirname of the file path i.e. one level above use:
os.path.dirname('file_path')
'''

create_path = os.path.join(os.environ.get('Path').split(';')[0], 'sanket.txt')
print(os.path.dirname(os.path.dirname(create_path)))

#%%

'''
to get the base name use: basename i.e. last name after /
'''

create_path = os.path.join(os.environ.get('Path').split(';')[0], 'sanket.txt')
print(os.path.basename(create_path))

#%%

'''
if you want both dirname and basename use split()
'''

create_path = os.path.join(os.environ.get('Path').split(';')[0], 'sanket')
print(os.path.split(create_path))

#%%
'''
if you want to check if path exist use os.path.exists
'''

create_path = os.path.join(os.environ.get('Path').split(';')[0], 'sanket')
print(os.path.exists(create_path))
print(os.path.exists(os.path.dirname(create_path)))

#%%
'''
if you want to check if a path is a directory or a file use: os.path.isdir() and os.path.isfile()
'''

path = os.path.join(r'E:\code\Haskell-workspace','practice.hs')
print(os.path.isdir(path))
print(os.path.isfile(path))

#%%%
'''
if you want to get the extension of the file use os.path.splitext()
'''

path = os.path.join(r'E:\code\Haskell-workspace','practice.hs')
print(os.path.splitext(path))

#%%
'''
to get the absolute path use: os.path.abspath()
'''
print(os.path.abspath('main.py'))

#%%
'''
os.path.getatime(path)
Return the time of last access of path. The return value is a number giving the number of seconds since the
 epoch (see the time module). Raise os.error if the file does not exist or is inaccessible.
 
you can also use os.stat
'''

print(os.path.getatime('sysmodule2/winter.csv'))

from datetime import datetime
print(datetime.fromtimestamp(os.path.getatime('sysmodule2')))

#%%
import glob
import os
# if you want to list all the files with common path pattern you can use glob.glob

files_dir = glob.glob('*/*')
print(files_dir)