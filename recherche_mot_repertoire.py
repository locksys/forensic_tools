'''Realise par Locksys le 24/01/2022'''

import os, sys
from stat import *
import time, datetime

def arborescence(top, keyword, callback):

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
	try: 
	    if S_ISDIR(mode):
		# Repertoire, recursivite 
	      	arborescence(pathname, keyword, callback)
	    elif S_ISREG(mode):
		#Ouverture du fichier puis recherche du keyword
	      	with open(pathname) as fichier :
 		   if keyword in fichier.read() :
		      callback(pathname, keyword)
	except OSError:
    	    print 'OSError : '+pathname
    	    pass

def printfile(file, chaine):
    print "Chaine :"+chaine+" -> Path : "+file

if __name__ == '__main__':
    if len(sys.argv) == 3 :
	   arborescence(sys.argv[1], sys.argv[2], printfile)
    else :
	print '\nUsage :  python2 recherche_mot.py <path-to-directory> <chaine> | ex: python2 recherche_mot.py repertoire/ chaine'

    
