"""Interface en ligne de commande.

    indexeur chercher DOSSIER "requête" [-k 10]
    indexeur stats DOSSIER
"""

import argparse
import sys

from indexeur.corpus import lire_dossier
from indexeur.index import Index
from indexeur.recherche import rechercher


def construire(dossier):
    index = Index()
    for nom, texte in lire_dossier(dossier).items():
        index.ajouter(nom, texte)
    return index


def commande_chercher(args):
    index = construire(args.dossier)
    for r in rechercher(index, args.requete, k=args.k):
        print(f"{r.score:8.3f}  {r.identifiant}")
    return 0


def commande_stats(args):
    index = construire(args.dossier)
    print(f"documents : {len(index)}")
    print(f"termes distincts : {len(index.postings)}")
    print(f"longueur moyenne : {index.longueur_moyenne():.1f} termes")
    return 0


def main(argv=None):
    parseur = argparse.ArgumentParser(prog="indexeur", description=__doc__.splitlines()[0])
    sous = parseur.add_subparsers(dest="commande", required=True)

    p = sous.add_parser("chercher", help="chercher dans un dossier de fichiers .txt")
    p.add_argument("dossier")
    p.add_argument("requete")
    p.add_argument("-k", type=int, default=10, help="nombre de résultats (défaut : 10)")
    p.set_defaults(fonction=commande_chercher)

    p = sous.add_parser("stats", help="statistiques sur un dossier")
    p.add_argument("dossier")
    p.set_defaults(fonction=commande_stats)

    args = parseur.parse_args(argv)
    return args.fonction(args)


if __name__ == "__main__":
    sys.exit(main())
