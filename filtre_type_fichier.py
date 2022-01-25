'''Realise par Locksys le 25/01/2022'''

import os, sys
from stat import *
import pathlib
import shutil
from pathlib import Path

def arborescence(top, extension, callback, dest):
    
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
	try : 
            mode = os.stat(pathname).st_mode
	    if S_ISDIR(mode):
		# Repertoire, recursivite 
	      	arborescence(pathname, extension, callback, dest)
	    elif S_ISREG(mode):
		path=pathlib.Path(pathname)
		if path.suffix == extension :
			callback(pathname, dest)
	except OSError :
    	    pass

def copyfile(file, dest):
	shutil.copy(file,dest)    

if __name__ == '__main__':
    if len(sys.argv) == 4 :
	if (os.path.isdir(sys.argv[2])) and (os.path.isdir(sys.argv[1])) :
    	#Verification que les repertoires donnees par l'utilisateur existe
		extension="."+sys.argv[3]
		arborescence(sys.argv[1], extension, copyfile, sys.argv[2])
	else :
		print 'Le repertoire '+sys.argv[1]+' ou '+sys.argv[2]+' est inexistant.'
    else :
	print '\nUsage :  python2 filtre_type_fichier.py <path-to-directory> <path-to-directory-result>  <extension> | ex: python2 filtre_type_fichier.py repertoire/ sortie/  txt'

    
