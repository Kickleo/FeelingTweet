import json
import os.path

i=0

while os.path.isfile("donnees"+str(i)+".json") :
    print("donnees"+str(i)+".json :")
    with open("donnees.json", "r") as mj :
        dict_ = json.load(mj)
        for key in dict_ :
            if (key == "statuses") :
                for key2 in dict_[key] :
                    for key3 in key2 :
                        if(key3 == "user") :
                            print(type(key3))
                            print(key3)
                            print(key2[key3])
                            for key4 in key2[key3] :
                                print(key4)
                        if(key3 == "contributors") :
                            print(type(key3))
                            print(key3)
                            print(key2[key3])
    i += 1