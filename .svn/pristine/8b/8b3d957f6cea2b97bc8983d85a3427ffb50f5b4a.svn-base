#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Init
print ('\n'+"---- Backito ----")
import sys, os, shutil, getpass, logging, glob, filecmp, ftplib
from shutil import copytree, copyfile
from crontab import CronTab
from funcs import remove_dir, make_dir, rec_backup, ftp_sendfile, ftp_rm_directory, ftp_create_directory1, ftp_create_directory2, tri_type_directory
from ftplib import FTP

# Revs
count = 0
thefile = open("/home/"+getpass.getuser()+"/backup/.backito", 'rb')
while 1:
    buffer = thefile.read(8192*1024)
    if not buffer: break
    count += buffer.count('\n')
thefile.close(  )

# GLOBAL Vars
if sys.argv[1][len(sys.argv[1]) - 1] != "/":
    file1 = sys.argv[1]
else:
    file1 = sys.argv[1][:-1]
filename = file1.split("/")[-1]
file2 = "/home/"+getpass.getuser()+"/backup/Backup_"+filename+"/"+filename
ftp = FTP('jivfdo.netne.net', 'a6932816', 'qwerty1')
pathftp = ftp.cwd('/backup/')

# Main
rec_backup(file1, file2)
if os.path.isdir(file1) == True:
    remove_dir(file1, file2)

print ("Revision: "+str(count)+'\n')

# LogFile
os.system("sshpass -p 'yskh' scp root@10.104.3.173:/home/student/backup/.backito /home/"+getpass.getuser()+"/backup/")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/home/'+getpass.getuser()+'/backup/.backito')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info('Success Backup : ['+file1+'] - Timing: 1')

os.system("sshpass -p 'yskh' rsync -avzh /home/"+getpass.getuser()+"/backup root@10.104.3.173:/home/student")

if os.path.isdir(file1) == 1:
	if ftp.nlst('/backup/Backup_' + filename):
		path2ftp = '/backup/Backup_' + filename
		ftp_rm_directory(path2ftp)
		ftp_create_directory1(filename, file1)
	else:
		ftp_create_directory1(filename, file1)
elif os.path.isfile(file1) == 1:
	ftp_sendfile(file1)