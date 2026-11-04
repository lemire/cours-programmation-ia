"""Sources de documents : un dossier de fichiers texte, ou un corpus
synthétique reproductible (pour les tests et les bancs d'essai)."""

import random
from pathlib import Path

SYLLABES = (
    "ba be bi bo bu ca ce ci co cu da de di do du fa fe fi fo fu la le li lo lu "
    "ma me mi mo mu na ne ni no nu pa pe pi po pu ra re ri ro ru sa se si so su "
    "ta te ti to tu va ve vi vo vu cha che chi cho chu tra tre tri tro tru"
).split()


def lire_dossier(dossier):
    """Les fichiers .txt d'un dossier : {nom du fichier: contenu}, triés par nom."""
    chemins = sorted(Path(dossier).glob("*.txt"))
    return {p.name: p.read_text(encoding="utf-8") for p in chemins}


def vocabulaire(taille, graine=0):
    """Un vocabulaire de mots inventés, toujours le même pour une graine donnée."""
    hasard = random.Random(graine)
    mots = set()
    while len(mots) < taille:
        mots.add("".join(hasard.choice(SYLLABES) for _ in range(hasard.randint(2, 4))))
    return sorted(mots)


def synthetique(nombre, mots_par_document=200, taille_vocabulaire=5000, graine=0):
    """Un corpus synthétique : {identifiant: texte}.

    La fréquence des mots suit approximativement une loi de Zipf, comme dans
    une vraie langue : quelques mots très fréquents, beaucoup de mots rares.
    """
    hasard = random.Random(graine)
    vocab = vocabulaire(taille_vocabulaire, graine)
    poids = [1.0 / (rang + 1) for rang in range(len(vocab))]
    corpus = {}
    for i in range(nombre):
        texte = " ".join(hasard.choices(vocab, weights=poids, k=mots_par_document))
        corpus[f"doc{i:06d}"] = texte
    return corpus
