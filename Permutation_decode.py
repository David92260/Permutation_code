#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Permutation decoding on an encoded input file
"""
import os
import numpy as np
from Tkinter import *
import unicodedata

infile = "Resultat.txt"
outfile= "Resultat_decode.txt"

code_dict = {
	'A': 'B',
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

decode_dict = {v: k for k, v in code_dict.iteritems()}

def strip_accents(text):
	try:
        	text = unicode(text, 'utf-8')
	except TypeError: # if text is already utf-8 
		pass
	text = unicodedata.normalize('NFD', text)
	text = text.encode('ascii', 'ignore')
	text = text.decode("utf-8")
	return str(text)

def decode(un_texte):
	"Takes a string, decodes it and returns the resulting string"
	un_texte = strip_accents(un_texte).upper()
	decoded_text = []
	for c in un_texte:
		if c in decode_dict:
			decoded_text.append(decode_dict[c])
		else:
			decoded_text.append(c)
	return "".join(decoded_text)


with open(infile, 'r') as f:
	read_data = f.read()

with open(outfile, 'w') as f:
    f.write(decode(read_data))


