#!/usr/bin/env python2

import os, sys, time, random, string

<<<<<<< ac4fd68e2f0de672761c2a38b9494dc652873231
#~ non_chrs = string.lowercase + string.whitespace
#~ chrs = [chrc for chrc in string.printable if chrc not in non_chrs]
=======
class bg:
    default = '\033[00m'
    red =  '\033[31m' + '\033[01m'
    green = '\033[32m' + '\033[01m'
    yellow = '\033[33m' + '\033[01m'
    blue =  '\033[34m' + '\033[01m'
    purple = '\033[35m' + '\033[01m'
    bluish = '\033[36m' + '\033[01m'
    white = '\033[37m' + '\033[01m'
    redb = '\033[41m'
    blueb = '\033[44m'
    greenb = '\033[42m'
    yellowb = '\033[43m'
    bluishb = '\033[46m'
    purpleb = '\033[45m'

>>>>>>> Update
chrs = string.digits + string.uppercase

def randomkey(length):
    return ''.join(random.choice(chrs) for i in range(length))

def vernam_enc(encs, key):
	op = ""
	for encs_bit, keys_bit in zip(encs, key):
		op += chr(int(ord(keys_bit)) ^ int(ord(encs_bit)))
	return op

def encrypt(encrypt_w, key):
	return vernam_enc(encrypt_w, key)

try:
	if sys.argv[1] == "-e":
		if sys.argv[3] == "-rkey":
			key = randomkey(len(sys.argv[2]))
			op = encrypt(sys.argv[2], key)
		elif sys.argv[3]:
			key = sys.argv[3]
		op = encrypt(sys.argv[2], key)
		print bg.blue + "Encrypted:  " + bg.default + bg.blueb + op + bg.default
		print bg.red + "      Key:  " + bg.default + bg.redb + key + bg.default
	elif sys.argv[1] == "-d":
		op = encrypt(sys.argv[2], sys.argv[3])
		print bg.yellow + "Decrypted: " + op + bg.default
except IndexError:
	print "Error: parameters not be empty."
