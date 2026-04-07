from arbreBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    
    def __init__(self, val=None, g=None, d=None):
        super().__init__(val, g, d)
    
    @staticmethod
    def frequences_lettres(chaine):
        freq = {}
        for c in chaine:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)  
        return freq
    
    @staticmethod
    def fusion(n1, n2):
        """Fusionne deux noeuds de Huffman en un nouveau noeud dont la valeur est la concaténation des valeurs des deux noeuds et le poids est la somme des poids des deux noeuds."""
        assert isinstance(n1, NoeudHuffman)
        assert isinstance(n2, NoeudHuffman)

        chaine_concatenee = n1.get_valeur()[0] + n2.get_valeur()[0]
        poids = n1.get_valeur()[1] + n2.get_valeur()[1]
        return NoeudHuffman((chaine_concatenee, poids), n1, n2)
    
    @staticmethod
    def construire_arbre(chaine):
        """Construit l'arbre de Huffman à partir d'une chaîne de caractères."""
        assert isinstance(chaine, str), "La variable chaine doit être une chaîne de caractères"
        liste_freq = NoeudHuffman.frequences_lettres(chaine)
        noeuds = []

        for c, f in liste_freq:
            noeuds.append(NoeudHuffman((c, f)))

        while len(noeuds) > 1:
            noeuds.sort(key=lambda n: n._valeur[1])
            n1 = noeuds.pop(0)
            n2 = noeuds.pop(0)

            fusion = NoeudHuffman.fusion(n1, n2)
            noeuds.append(fusion)

        return noeuds[0]

    def generer_codes(self, code="", dico=None):
            if dico is None:
                dico = {}

            if self.est_feuille():
                caractere = self.get_valeur()[0]
                dico[caractere] = code
                return dico

            if self.possede_gauche():
                self.get_gauche().generer_codes(code + "0", dico)

            if self.possede_droit():
                self.get_droit().generer_codes(code + "1", dico)

            return dico

    @staticmethod
    def compression(chaine, codes):
        """Compresse une chaîne de caractères en utilisant les codes de Huffman générés à partir de l'arbre de Huffman."""
        res = ""

        for c in chaine:
            res += codes[c]
        return res

    @staticmethod
    def decompression(chaine_compressee, arbre):
        """Décompresse une chaîne de caractères compressée en utilisant l'arbre de Huffman."""
        chaine_decodee = ""
        noeud_courant = arbre

        for val in chaine_compressee:
            if val == "0":
                noeud_courant = noeud_courant.get_gauche()
            else :
                noeud_courant = noeud_courant.get_droit()
            
            if noeud_courant.est_feuille():
                chaine_decodee += noeud_courant.get_valeur()[0]
                noeud_courant = arbre
        return chaine_decodee
