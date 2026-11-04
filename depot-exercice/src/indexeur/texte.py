"""Découpage d'un texte en termes.

Un *terme* est un mot normalisé : en minuscules, sans accents, et qui n'est
pas un mot vide. Toute la suite (index, requêtes) ne voit que des termes.
"""

import re
import unicodedata

MOTS_VIDES = frozenset(
    """
    a au aux avec ce ces dans de des du elle en et eux il ils je la le les
    leur lui ma mais me meme mes moi mon ne nos notre nous on ou par pas pour
    qu que qui sa se ses son sur ta te tes toi ton tu un une vos votre vous
    c d j l m n s t y est sont ete etre avoir ont
    """.split()
)


def sans_accents(mot):
    """Retire les accents : « Élève » devient « Eleve »."""
    decompose = unicodedata.normalize("NFD", mot)
    return "".join(c for c in decompose if unicodedata.category(c) != "Mn")


def normaliser(mot):
    """Met un mot sous sa forme normale : minuscules, sans accents."""
    mot = mot.lower()
    mot = mot.replace("œ", "oe").replace("æ", "ae")
    return sans_accents(mot)


def mots(texte):
    """Les mots d'un texte, dans l'ordre, sans normalisation."""
    return re.findall(r"\w+", texte)


def termes(texte):
    """Les termes d'un texte, dans l'ordre, mots vides retirés."""
    resultat = []
    for mot in mots(texte):
        terme = normaliser(mot)
        if terme not in MOTS_VIDES and not terme.isdigit():
            resultat.append(terme)
    return resultat
