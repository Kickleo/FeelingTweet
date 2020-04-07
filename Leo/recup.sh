#!/bin/sh

echo "récupération des données concernant le coronavirus";
python3 recuperateur_de_données.py Coronavirus Coronavirus1>/dev/null;
echo "fait."
sleep 1;
echo "récupération des données concernant l'E32020";
python3 recuperateur_de_données.py E32020 E32020  >/dev/null;
echo "fait."
sleep 1;
echo "récupération des données concernant Fillon";
python3 recuperateur_de_données.py Fillon Fillon  >/dev/null;
echo "fait."
sleep 1;
echo "récupération des données concernant Macron";
python3 recuperateur_de_données.py Macron Macron  >/dev/null;
echo "fait."
sleep 1;
echo "récupération des données concernant le moi des droits de la femme";
python3 recuperateur_de_données.py MoisDesDroitsDeLaFemme  MoisDesDroitsDeLaFemme >/dev/null;
echo "fait."
sleep 1;
echo "récupération des données concernant le Football";
python3 recuperateur_de_données.py Football Football  >/dev/null;
echo "fait."