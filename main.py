from NoeudHuffman import NoeudHuffman
from unidecode import unidecode
import sys
import os

dossier_input = sys.argv[1]

#Parcours des fichiers du dossier input
for fichier in os.listdir(dossier_input):
    if fichier.endswith(".txt"):
        f_path = os.path.join(dossier_input, fichier)
        with open(f_path, 'r', encoding='utf-8') as file:
            contenuTxt = file.read()
            contenuTxt = unidecode(contenuTxt)

            print(f"\nFichier {fichier} chargé.")

            #Conversion en binaire
            binaire_initial = NoeudHuffman.chaine_vers_binaire(contenuTxt)

            #Construction de l'arbre de Huffman et compression
            arbre = NoeudHuffman.construire_arbre(contenuTxt)
            codes = arbre.generer_codes()
            chaine_compressee = NoeudHuffman.compression(contenuTxt, codes)
