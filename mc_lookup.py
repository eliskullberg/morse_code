#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
mc_lookup.py: Converts Enlish letters to ITU-style morse. 

'''
__author__ = "Elis Kullberg"
__copyright__ = "Copyright 2012, Morse Code translator"
__credits__ = ["None"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Elis Kullberg"
__email__ = "elis@eliskullberg.com"
__status__ = "Testing"


def string_to_morse(string):
    morsestring = map(char_to_morse,string)
    return " ".join(morsestring)


def morse_to_string(morsestring):
    morselist = morsestring.split(" ")
    letterlist = [morse_to_char(c) for c in morselist]
    return "".join(letterlist)


def char_to_morse(letter):
    try:
        return "{0}".format(str(letter2morse[letter]))
    except KeyError:
        raise LookupWhoops


def morse_to_char(morse):
    try:
        return "{0}".format(str(morse2letter[morse]))
    except KeyError:
        raise LookupWhoops


letter2morse = {"A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    " ":" ",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "9":"-----"}

morse2letter = dict(zip(letter2morse.values(), letter2morse.keys()))


class LookupWhoops(Exception):
    # TODO: Implement
    pass
