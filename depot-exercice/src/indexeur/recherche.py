"""La recherche : trouver les documents qui contiennent tous les termes d'une
requête, et les classer par pertinence (BM25)."""

import math
from dataclasses import dataclass

from indexeur.texte import termes

# Paramètres usuels de BM25 (Robertson et Zaragoza, 2009).
K1 = 1.2
B = 0.75


@dataclass(frozen=True)
class Resultat:
    identifiant: str
    score: float


def idf(index, terme):
    """Rareté d'un terme : élevée pour un terme rare, faible pour un terme fréquent."""
    n = len(index)
    df = len(index.documents_avec(terme))
    return math.log((n - df + 0.5) / (df + 0.5) + 1.0)


def score_bm25(index, termes_requete, identifiant):
    """Le score BM25 d'un document pour une requête."""
    score = 0.0
    for terme in termes_requete:
        tf = index.frequence(terme, identifiant)
        longueur = index.longueurs[identifiant]
        norme = K1 * (1 - B + B * longueur / index.longueur_moyenne())
        score += idf(index, terme) * tf * (K1 + 1) / (tf + norme)
    return score


def intersection(listes):
    """Les éléments communs à toutes les listes, dans l'ordre de la première."""
    if not listes:
        return []
    commun = listes[0]
    for autre in listes[1:]:
        commun = [x for x in commun if x in autre]
    return commun


def rechercher(index, requete, k=10):
    """Les k documents les plus pertinents qui contiennent tous les termes.

    Les résultats sont triés par score décroissant; à score égal, par
    identifiant croissant, pour que la sortie soit déterministe.
    """
    termes_requete = termes(requete)
    if not termes_requete:
        return []
    candidats = intersection([index.documents_avec(t) for t in termes_requete])
    resultats = [Resultat(d, score_bm25(index, termes_requete, d)) for d in candidats]
    resultats.sort(key=lambda r: (-r.score, r.identifiant))
    return resultats[:k]
