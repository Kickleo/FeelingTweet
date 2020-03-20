import os
import sys
import re

mots=" "
for mot in sys.argv :
    if (mot != sys.argv[0]) :
        mots += mot +" " 


os.system('python3 recuperateur_de_donnees.py'+mots)
os.system('python3 twitter.py')
