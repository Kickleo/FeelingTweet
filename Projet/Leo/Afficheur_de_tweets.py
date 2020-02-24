import json
import os.path

i=0

while os.path.isfile("donnees"+str(i)+".json") :
    print("donnees"+str(i)+".json :")
    i += 1
