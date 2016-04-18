#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Init
import sys, os, shutil, getpass, logging, glob, filecmp, ftplib, sys, os
from shutil import copytree, copyfile
from crontab import CronTab
from ftplib import FTP

# GLOBAL Vars
if sys.argv[1][len(sys.argv[1]) - 1] != "/":
    file1 = sys.argv[1]
else:
    file1 = sys.argv[1][:-1]
filename = file1.rsplit('/', 1)[-1]
print filename
file2 = "/home/"+getpass.getuser()+"/backup/Backup_"+filename+"/"+filename

ftp = FTP('jivfdo.netne.net', 'a6932816', 'qwerty1')
pathftp = ftp.cwd('/backup/')

# -------------------------- Recursive Funcs --------------------------

def remove_dir(file1, file2):
    list1 = os.listdir(file1)
    list2 = os.listdir(file2)
    for file in list2:
        if file[0] == ".":
            continue
        elif not file in list1:
            if os.path.isdir(file2+"/"+file):
                print("[D] - "+file+" ( "+file2+"/"+file+"/* )")
                shutil.rmtree(file2+"/"+file)
            else:
                print("[D] - "+file+" ( "+file2+"/"+file+" )")
                os.remove(file2+"/"+file)
        else:
            if os.path.isdir(file):
                remove_dir(file1+"/"+file, file2+"/"+file)
    pass

def make_dir(file1, file2, file):
    print("[A] - "+file+" ( "+file2+"/ )")
    os.mkdir(file2)
    list1 = os.listdir(file1)
    for file in list1:
        if os.path.isdir(file1+"/"+file):
            make_dir(file1+"/"+file, file2+"/"+file, file)
        elif os.path.isfile(file1+"/"+file):
            print("[A] - "+file+" ( "+file2+"/"+file+" )")
            copyfile(file1+"/"+file, file2+"/"+file)
    pass

def rec_backup(file1, file2):
    if os.path.isdir(file1) == True:
        list1 = os.listdir(file1)
        list2 = os.listdir(file2)
        for file in list1:
            if file[0] == ".":
                continue
            elif os.path.isdir(file1+"/"+file) and file in list2:
                rec_backup(file1+"/"+file, file2+"/"+file)
            elif os.path.isfile(file1+"/"+file) and file in list2:
                if filecmp.cmp(file1+"/"+file, file2+"/"+file, shallow=False) == False:
                    print ("[U] - "+file+" ( "+file2+" )")
                    copyfile(file1+"/"+file, file2+"/"+file)
            else:
                if os.path.isdir(file1+"/"+file):
                    make_dir(file1+"/"+file, file2+"/"+file, file)
                elif os.path.isfile(file1+"/"+file):
                    print("[A] - "+file+" ( "+file2+" )")
                    copyfile(file1+"/"+file, file2+"/"+file)
    else:
        if filecmp.cmp(file1, file2, shallow=False) == False:
            copyfile(file1, file2)
            print ("[U] - "+filename)
    pass

# ---------------------------------------------------------------------

# -------------------------- Recursive Funcs --------------------------
def download_from_ftp():
    print "etape2"
    pass

def ftp_sendfile(file1):
    ftp = FTP('jivfdo.netne.net', 'a6932816', 'qwerty1')
    ftp.cwd('/backup/')
    myfile = open(file1, 'rb')
    ftp.storbinary('STOR ' + 'Backup' + file1, myfile)
    pass

def ftp_rm_directory(path2ftp):
    try:
        ftp.delete(path2ftp)
    except ftplib.error_perm:
        ftp.cwd(path2ftp)
        for finded in ftp.nlst():
            if finded not in ['.','..']:
                ftp_rm_directory(finded)
        ftp.cwd('..')       
        ftp.rmd(path2ftp)
    pass

def ftp_create_directory1(filename, file1):
    ftpdir = "Backup_" + filename
    ftp.mkd(ftpdir)
    ftp.cwd(ftpdir)
    ftp.mkd(filename)
    ftp.cwd(filename)
    list1 = []
    list1 = tri_type_directory(file1)
    for finded in list1:
        if os.path.isdir(file1+'/'+finded) == 1:
            ftp_create_directory2(file1+'/'+finded)
        elif os.path.isfile(file1+'/'+finded) == 1:
            myfile = open(file1+'/'+finded, 'rb')
            ftp.storbinary('STOR ' + finded, myfile)
    pass

def ftp_create_directory2(file1):
    path = '/backup/'+'Backup_'+filename+'/'
    ftp.mkd(path+file1)
    list1 = tri_type_directory(file1)
    for finded in list1:
        if os.path.isdir(file1+'/'+finded) == 1:
            ftp_create_directory2(file1+'/'+finded)
        elif os.path.isfile(file1+'/'+finded) == 1:
            myfile = open(file1+'/'+finded, 'rb')
            ftp.storbinary('STOR '+path+file1+'/'+finded, myfile)
    pass

def tri_type_directory(file1):
    listdef = []
    list11 = os.listdir(file1)
    for filefinded in list11:
        if os.path.isfile(file1+'/'+filefinded) == 1:
            listdef.append(filefinded)
    for dirfinded in list11:
        if os.path.isdir(file1+'/'+dirfinded) == 1:
            listdef.append(dirfinded)
    return listdef  
    pass    
# ---------------------------------------------------------------------