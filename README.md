# forensic_tools

Collection de script que j'ai crée et utilisé lors d'invesgation numérique.

filtre_repertoire_avec_date.py :
  Il permet de lister tous les fichiers d'un répertoire qui ont été modifié et/ou accédé après la date choisie en entrée.
  
    Usage : python2 filtre_repertoire_avec_date.py <chemin-vers-le-repertoire> <date-format %DD/%MM/%YYYY> <option>
  
    Option : 0 -> Retourne la liste des fichiers du répertoire qui ont été modifié et accédé
           1 -> Retourne la liste des fichiers du répertoire qui ont été modifié
           2 -> Retourne la liste des dichiers du répertoire qui ont été accédé
  
recherche_mot_repertoire.py :
    Il a permet de lister tous les fichiers d'un répertoire qui possède la chaîne de caractère donnée en argument du programme.
    
     Usage : python2 recherche_mot_repertoire.py <chemin-vers-le-repertoire> <chaine-a-rechercher>

filtre_type_fichier.py :
    Il permet de copier dans un répertoire de sortie l'ensemble des fichiers d'un répertoire possédant le type choisi.

     Usage : python2 filtre_type_fichier.py <chemin-vers-le-repertoire-a-analyser> <chemin-vers-le-repertoire-de-sortie> <extension> 
