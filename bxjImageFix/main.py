#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import re
import os.path
import shutil

def renImage( strLink,id,index ):
    searchObj = re.search( r'=Hyperlink\((.*)，"(.*)"\)', strLink, re.M|re.I)
    if searchObj:
        url = searchObj.group(2);
        ext = os.path.splitext(url)[1];
        filename = '_local/src/'+searchObj.group(2);
        if os.path.exists(filename):
            #print searchObj.group(2),id+'-'+index+ext;
            saveFilename = '_local/images/%04d-%s%s' % (int(id),index,ext);

            if os.path.exists(saveFilename):
                print '目标文件',saveFilename,' is exists;';
            else:
                print '复制文件',saveFilename,'OK;';
                shutil.copyfile(filename,saveFilename);
        else:
            print '源文件',filename,' is not exists;';
    return;


fileName = '_local/data/1131368_seg_1.csv';
fo = open(fileName, 'r');
reader = csv.reader(fo)
for line in reader:
    if line[0].isdigit():
        if int(line[0])>200:
            renImage( line[33],line[0],'1' );
            renImage( line[34],line[0],'2' );
            renImage( line[35],line[0],'3' );
'''
        searchObj = re.search( r'=Hyperlink\((.*)，"(.*)"\)', line[33], re.M|re.I)
        if searchObj:
            print searchObj.group(2),line[0],'-1';
        searchObj = re.search( r'=Hyperlink\((.*)，"(.*)"\)', line[34], re.M|re.I)
        if searchObj:
            print searchObj.group(2),line[0],'-2';
        searchObj = re.search( r'=Hyperlink\((.*)，"(.*)"\)', line[35], re.M|re.I)
        if searchObj:
            print searchObj.group(2),line[0],'-3';
'''
