# SAE202 BUT Informatique, IUT de Créteil-Vitry

Implémentation en Python de l'algorithme de **codage de Huffman**, permettant la compression et décompression de fichiers texte sans perte de données.

## Exécution du projet
```bash
python3 main.py input/
```

## Fonctionnalités
- Lecture de fichiers txt
- Construction d'un arbre de Huffman à partir des fréquences de caractères
- Encodage (compression) du texte
- Décodage (décompression) pour vérification
- Affichage taux comparatif des tailles avant/après compression

## Principe de Huffman
L'algorithme attribue des codes courts binaires aux caractères fréquents et des codes longs aux caractères rares réduisant ainsi la taille globale du fichier.

Étapes :
1. Calcul des fréquences de chaque caractère
2. Construction de l'arbre de Huffman (par fusions successives)
3. Génération des codes binaires (parcours de l'arbre)
4. Compression du texte avec ces codes

### NoeudBinaire.py
Implémentation d'un arbre binaire avec :
- création de noeuds, accès gauche/droite
- vérification feuille / arbre vide
- calcul de hauteur
- parcours préfixe, infixe, suffixe et en largeur

### NoeudHuffman.py
Hérite de arbre_binaire.py et ajoute :
- stockage des fréquences
- construction de l'arbre de Huffman
- génération des codes binaires

### main.py
- Lecture du dossier input
- Orchestration de la compression
- Affichage des résultats
 possibles
