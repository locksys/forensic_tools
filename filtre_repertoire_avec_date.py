'''Realise par Locksys le 24/01/2022'''

import os, sys
from stat import *
import time, datetime

def arborescence(top, date, callback, type):
    '''Recursivite dans le repertoire choisi, de haut en bas'''
    timestamp=time.mktime(datetime.datetime.strptime(date,"%d/%m/%Y").timetuple())

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
	try: 
	    if S_ISDIR(mode):
		# Repertoire, recursivite 
		if type == 1 :
	      	    arborescence(pathname, date, callback, 1)
	        elif type == 2 :
		    	arborescence(pathname, date, callback, 2)
	    elif S_ISREG(mode):
	         #Fichier, on affiche la date 
	        if type == 1 :
	            if os.stat(pathname).st_mtime > timestamp :
			       #Fichier modifie apres la date choisie en entree   
			       date_file=time.ctime(os.stat(pathname).st_mtime)
			       callback(pathname, date_file)
	        elif type == 2 :
		        if os.stat(pathname).st_atime > timestamp :
		           #Dernier acces au fichier apres la date choisie en entree 
		           date_file=time.ctime(os.stat(pathname).st_atime)
		           callback(pathname, date_file)
	    else :
	        #Fichier inconnu
	        print('Fichier Inconnu '+ pathname)
    except OSError:
    	print'OSError : '+pathname
    	pass

def printfile(file, date):
    print 'Modifie le : '+date+" Path : "+file

def printaccess(file, date):
    print 'Dernier acces le : '+date+' Path : '+file

if __name__ == '__main__':
    if len(sys.argv) == 4 :
	print '\n---------- Liste des fichiers trouves ----------'	 
	if sys.argv[3] == '0' :
	    arborescence(sys.argv[1], sys.argv[2], printfile, 1)
	    print '---------- Fin de la liste pour la derniere modification ----------\n'
	    arborescence(sys.argv[1], sys.argv[2], printaccess, 2)
	    print '--------- Fin de la liste pour le dernier acces --------'
	elif sys.argv[3] == '1' :
	    arborescence(sys.argv[1], sys.argv[2], printfile, 1)
	elif sys.argv[3] == '2' :
	    arborescence(sys.argv[1], sys.argv[2], printaccess, 2)
	else : 
	    print 'Option invalide'
	print '---------- Fin --------'
    else :
	print '\nUsage :  python2 liste_date_file.py <path-to-directory> <date> <option> | ex: python2 last_modif.py repertoire/ 01/01/2021 0'
	print '\nOption : 0 - toutes les options | 1 - Derniere modification | 2 - Dernier acces' 
    
