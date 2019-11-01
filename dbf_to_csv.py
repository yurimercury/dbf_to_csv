#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:46:50 2019

@author: patolog
"""

print('start')
import csv, os, sys, dbf

input_path = r'/home/patolog/Desktop/input'
output_path = r'/home/patolog/Desktop/output'

for dirpath, dirnames, filenames in os.walk(input_path):
    print (filenames)
    for filename in filenames:
        if filename.endswith('.dbf'):
            print('Converting to csv', filename)
            csv_fnl = filename[:-4] + '.csv'
            csv_fn = os.path.join(output_path, csv_fnl)
            
            with open(csv_fn, 'w') as csvfile:
                in_db = dbf.Dbf(os.path.join(dirpath, filename))
                out_csv = csv.writer(csvfile)
                names = []
                for field in in_db.header.fields:
                    names.append(field.name)
                out_csv.writerow(names)
                for rec in in_db:
                    out_csv.writerow(rec.fieldData)
                in_db.close()
                print('Done...')