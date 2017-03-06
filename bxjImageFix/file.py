#!/usr/bin/python
# -*- coding: UTF-8 -*-

fileName = '1131368_seg_1.csv';
fo = open(fileName, 'r');
# fileContent = fo.read();

try:
    for i in range(1000):
        line = fo.next()
        print line
except StopIteration:
    print 'here is end ',i

#print fileContent;
