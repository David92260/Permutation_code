#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Permutation encoding
"""
import os
import numpy as np
from Tkinter import *
import unicodedata

#infile = "Test.txt"

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
	'Z': 'A',
	' ': ' '}

def strip_accents(text):
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def encode(un_texte):
	"Takes a string, encodes it and returns the resulting string"
	un_texte = strip_accents(un_texte).upper()
	coded_text = []
	for c in un_texte:
		coded_text.append(code[c])
	return "".join(coded_text)

def close_window():
    global entry
    entry = entree.get()
    fenetre.destroy()

#with open(infile, 'r') as f:
#	read_data = f.read()
#	print(read_data)
#	print(encode(read_data))

fenetre = Tk()

value = StringVar() 
value.set("texte a coder")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

label = Label(fenetre, text="Appuyez sur Valider pour enregistrer le texte à coder")
label.pack()

bouton = Button(fenetre, text="Valider", command=close_window)
bouton.pack()

fenetre.mainloop()

print("texte à coder: %s" % entry.encode('utf8'))
print("texte encodé:  %s" % encode(entry).encode('utf8'))



