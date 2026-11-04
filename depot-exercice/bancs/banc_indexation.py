"""Banc d'essai : temps d'indexation et de recherche sur un corpus synthétique.

    python bancs/banc_indexation.py                # valeurs par défaut
    python bancs/banc_indexation.py --documents 5000 --repetitions 7

Ce banc est volontairement simple. Il fait partie de ce que vous aurez à
critiquer et à améliorer au bloc 3 du cours.
"""

import argparse
import statistics
import time

from indexeur.corpus import synthetique
from indexeur.index import Index
from indexeur.recherche import rechercher



def indexer(corpus):
    index = Index()
    for identifiant, texte in corpus.items():
        index.ajouter(identifiant, texte)
    return index


def chronometrer(fonction, repetitions):
    durees = []
    for _ in range(repetitions):
        debut = time.perf_counter()
        fonction()
        durees.append(time.perf_counter() - debut)
    return durees


def main():
    parseur = argparse.ArgumentParser()
    parseur.add_argument("--documents", type=int, default=2000)
    parseur.add_argument("--mots", type=int, default=200)
    parseur.add_argument("--repetitions", type=int, default=5)
    args = parseur.parse_args()

    corpus = synthetique(args.documents, mots_par_document=args.mots)
    index = indexer(corpus)
    vocab = sorted(index.postings, key=lambda t: -len(index.postings[t]))
    requetes = vocab[:3] + [f"{vocab[0]} {vocab[1]}", f"{vocab[10]} {vocab[50]}"]

    t_index = chronometrer(lambda: indexer(corpus), args.repetitions)
    t_requetes = chronometrer(lambda: [rechercher(index, q) for q in requetes], args.repetitions)

    print(f"corpus : {args.documents} documents de {args.mots} mots")
    for nom, durees in [("indexation", t_index), ("5 requêtes", t_requetes)]:
        print(
            f"{nom:>12} : médiane {statistics.median(durees) * 1000:9.2f} ms"
            f"   min {min(durees) * 1000:9.2f} ms   max {max(durees) * 1000:9.2f} ms"
        )


if __name__ == "__main__":
    main()
