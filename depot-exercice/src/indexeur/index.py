"""L'index inversé : pour chaque terme, les documents qui le contiennent."""

from indexeur.texte import termes


class Index:
    """Un index inversé en mémoire.

    Pour chaque terme, on garde la liste des identifiants des documents qui le
    contiennent (dans l'ordre d'ajout) et, pour chaque couple (terme,
    document), le nombre d'occurrences.
    """

    def __init__(self):
        self.documents = {}  # identifiant -> texte original
        self.longueurs = {}  # identifiant -> nombre de termes
        self.postings = {}  # terme -> [identifiant, ...]
        self.frequences = {}  # (terme, identifiant) -> nombre d'occurrences

    def ajouter(self, identifiant, texte):
        """Ajoute un document. Un identifiant déjà présent est refusé."""
        if identifiant in self.documents:
            raise ValueError(f"document déjà indexé : {identifiant!r}")
        liste = termes(texte)
        self.documents[identifiant] = texte
        self.longueurs[identifiant] = len(liste)
        for terme in liste:
            if terme not in self.postings:
                self.postings[terme] = []
            if identifiant not in self.postings[terme]:
                self.postings[terme].append(identifiant)
            cle = (terme, identifiant)
            self.frequences[cle] = self.frequences.get(cle, 0) + 1

    def __len__(self):
        return len(self.documents)

    def __contains__(self, identifiant):
        return identifiant in self.documents

    def documents_avec(self, terme):
        """Les identifiants des documents qui contiennent le terme."""
        return self.postings.get(terme, [])

    def frequence(self, terme, identifiant):
        """Le nombre d'occurrences du terme dans le document."""
        return self.frequences.get((terme, identifiant), 0)

    def longueur_moyenne(self):
        """Le nombre moyen de termes par document."""
        if not self.longueurs:
            return 0.0
        return sum(self.longueurs.values()) / len(self.longueurs)
