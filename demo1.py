# -*- coding: utf-8 -*-

from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk

Font = ("simhei", "16")
f = open('The Making of Isaac Newton.txt')
data = f.readlines()
del data[0]

for d in data:
    if d!='\n':
        line = d.strip()
        with open('Isac Newton new.txt','a') as f:
            f.write(line)

def read():
    global results
    results = []
    f = open('Isac Newton new.txt')
    data = f.readlines()
    for d in data:
        info = d.split(' ')
        for inf in info:
            result = inf.replace(',','').replace('.','').strip().lower()
            results.append(result)
    return results

