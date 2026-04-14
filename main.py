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

            
            # Affichage
            print("Binaire ASCII :", binaire_initial[:100], "...")
            print("Compressé :", chaine_compressee[:100], "...")

            # Tailles de la chaine initiale et compressée
            taille_initiale = len(binaire_initial)
            taille_compressee = len(chaine_compressee)

            # Calcul et affichage du taux de compression
            taux = (1 - taille_compressee / taille_initiale) * 100

            print(f"Taille initiale : {taille_initiale} bits")
            print(f"Taille compressée : {taille_compressee} bits")
            print(f"Taux : {taux:.2f}%")

            # Décompression et vérification
            decomp = NoeudHuffman.decompression(chaine_compressee, arbre)
            print("Décompression OK" if decomp == contenuTxt else "Erreur")
