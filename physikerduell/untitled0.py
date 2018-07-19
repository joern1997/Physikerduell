#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 18:22:48 2018

@author: joern
"""

import csv
import numpy as np
i=0
Fragen = np.array([])
reader = csv.reader(open("Katalog01.csv"))
for row in reader:
    if (row[0] == ""):
        del(row[0])
    else:
        Fragen = np.append( Fragen ,row[0])
        i=i+1

print(Fragen)