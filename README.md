# SAE202 – Compression de texte avec Huffman

BUT Informatique, IUT de Créteil-Vitry

Implémentation en Python de l'algorithme de **codage de Huffman**, permettant la compression et décompression de fichiers texte sans perte de données.

## Exécution du projet
```bash
python3 main.py input/
```
## Comment le projet marche ?
Le programme se lance depuis le terminal en lui passant un dossier contenant des fichiers `.txt`. Il parcourt chaque fichier, analyse la fréquence d'apparition de chaque caractère, puis construit un arbre de Huffman pour générer des codes binaires optimisés. Le texte est ensuite compressé caractère par caractère en utilisant ces codes. À la fin, le programme affiche la taille du texte avant et après compression, ainsi que le gain obtenu. Une décompression est également effectuée pour vérifier que le texte reconstruit est identique à l'original.

## Fonctionnalités
- Lecture de fichiers `.txt`
- Construction d'un arbre de Huffman à partir des fréquences de caractères
- Encodage (compression) du texte
- Décodage (décompression) pour vérification
- Affichage comparatif des tailles avant/après compression

## Principe de Huffman
L'algorithme attribue des codes binaires **courts** aux caractères **fréquents** et des codes **longs** aux caractères **rares**, réduisant ainsi la taille globale du fichier.

**Étapes :**
1. Calcul des fréquences de chaque caractère
2. Construction de l'arbre de Huffman (par fusions successives)
3. Génération des codes binaires (parcours de l'arbre)
4. Compression du texte avec ces codes

## Structure du projet

├── input/               # Fichiers texte à compresser <br>
├── NoeudBinaire.py      # Arbre binaire générique <br>
├── NoeudHuffman.py      # Arbre de Huffman + compression <br>
├── main.py              # Point d'entrée du programme <br>
└── README.md

### `NoeudBinaire.py`
Implémentation d'un arbre binaire avec :
- création de nœuds, accès gauche/droite
- vérification feuille / arbre vide
- calcul de hauteur
- parcours préfixe, infixe, suffixe et en largeur

### `NoeudHuffman.py`
Hérite de `NoeudBinaire.py` et ajoute :
- stockage des fréquences
- construction de l'arbre de Huffman
- génération des codes binaires

### `main.py`
- Lecture du dossier `input/`
- Orchestration de la compression
- Affichage des résultats

---

## Utilisation

```bash
python3 main.py input/
```

### Exemple de sortie

```
Fichier input/test.txt chargé.
Construction de l'arbre de Huffman OK.
Compression OK.

Taille initiale   : 16312 bits
Taille compressée : 9187 bits
Gain              : ~43%
```

---

## Prérequis

- Python 3.x
- Module `unidecode` :

```bash
pip install unidecode
```

---

## Auteur
Valentin CARPINTEIRO-LERICQ
Assane DIEBATE
Nohlan MOMPEROUSSE
Arthur SIVAULT--LE MORELLEC
Projet réalisé dans le cadre de la SAÉ 2.02  
BUT Informatique – IUT de Créteil-Vitry
