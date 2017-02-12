#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Permutation encoding on an input file
"""
import os
import numpy as np
from Tkinter import *
import unicodedata

infile = "Test.txt"

code = {'A': 'B',
	'B': 'C',
	'C': 'D',
	'D': 'E',
	'E': 'F',
	'F': 'G',
	'G': 'H',
	'H': 'I',
	'I': 'J',
	'J': 'K',
	'K': 'L',
	'L': 'M',
	'M': 'N',
	'N': 'O',
	'O': 'P',
	'P': 'Q',
	'Q': 'R',
	'R': 'S',
	'S': 'T',
	'T': 'U',
	'U': 'V',
	'V': 'W',
	'W': 'X',
	'X': 'Y',
	'Y': 'Z',
	'Z': 'A'}

def strip_accents(text):
	try:
        	text = unicode(text, 'utf-8')
	except TypeError: # if text is already utf-8 
		pass
	text = unicodedata.normalize('NFD', text)
	text = text.encode('ascii', 'ignore')
	text = text.decode("utf-8")
	return str(text)

def encode(un_texte):
	"Takes a string, encodes it and returns the resulting string"
	un_texte = strip_accents(un_texte).upper()
	coded_text = []
	for c in un_texte:
		if c in code:
			coded_text.append(code[c])
		else:
			coded_text.append(c)
	return "".join(coded_text)


with open(infile, 'r') as f:
	read_data = f.read()
	print(read_data)
	print(encode(read_data))

#print("texte à coder: %s" % entry.encode('utf8'))
#print("texte encodé:  %s" % encode(entry).encode('utf8'))



