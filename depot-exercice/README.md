# indexeur

Un petit moteur de recherche plein texte, en français, écrit en Python pur
(aucune dépendance à l'exécution). C'est le dépôt d'exercice du cours
*Programmation assistée par l'IA* (TÉLUQ) : un vrai programme, petit, testé,
qui a une architecture et des défauts.

```console
$ uv run indexeur chercher exemples "sirop érable"
   2.257  erabliere.txt
   2.210  tire.txt
$ uv run indexeur stats exemples
documents : 6
termes distincts : 122
longueur moyenne : 24.0 termes
```

## Installer et vérifier

Il faut Python 3.10 ou plus récent et [uv](https://docs.astral.sh/uv/).

```bash
uv run pytest                          # les tests (quelques dixièmes de seconde)
uv run python bancs/banc_indexation.py # le banc d'essai (quelques secondes)
```

Sans uv : `python -m venv .venv`, activer l'environnement, puis
`pip install -e . pytest` et `pytest`.

## Organisation

Voir [ARCHITECTURE.md](ARCHITECTURE.md) : les modules, leurs responsabilités
et les règles que le code respecte.

## Demandes en attente

Ces demandes viennent d'utilisateurs. Elles sont volontairement formulées
comme le sont les vraies demandes : de manière incomplète. Le cours les
utilise comme matière première.

1. « Ce serait bien de pouvoir chercher une expression exacte, entre
   guillemets, comme `"cabane à sucre"`. »
2. « J'aimerais une sortie JSON pour brancher l'outil sur autre chose. »
3. « L'indexation est lente dès qu'on a quelques milliers de documents. »
4. « Il faudrait pouvoir sauvegarder l'index pour ne pas tout recalculer à
   chaque fois. »
5. « La recherche ne trouve pas *chevaux* quand je cherche *cheval*. »
6. « Ajouter la recherche avec OU, pas seulement ET. »
7. « Pouvoir retirer un document de l'index. »
8. « Afficher un extrait du document autour des mots trouvés. »

## Licence

Apache 2.0.
