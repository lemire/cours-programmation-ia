# Architecture

Le code est dans `src/indexeur/`. Les dépendances vont dans un seul sens :

```
cli  ──►  recherche  ──►  index  ──►  texte
  │                                     ▲
  └──►  corpus                          │
              recherche ────────────────┘
```

| Module | Responsabilité | Ne fait pas |
|---|---|---|
| `texte.py` | découper un texte en *termes* (minuscules, sans accents, sans mots vides) | ne connaît ni les documents ni l'index |
| `index.py` | l'index inversé : terme → documents, fréquences, longueurs | ne classe pas, ne lit pas de fichiers |
| `recherche.py` | trouver les documents qui contiennent tous les termes, les classer (BM25) | ne modifie jamais l'index |
| `corpus.py` | produire des documents : dossier de `.txt`, corpus synthétique | ne connaît pas l'index |
| `cli.py` | la ligne de commande, l'affichage | aucune logique de recherche |

## Règles

1. **Une seule normalisation.** Le texte des documents et celui des requêtes
   passent par la même fonction, `texte.termes`. Toute nouvelle
   transformation (racinisation, synonymes…) s'ajoute là, et nulle part
   ailleurs.
2. **Pas d'entrées-sorties hors de `cli.py` et `corpus.py`.** Les autres
   modules ne lisent ni n'écrivent de fichiers et n'affichent rien.
3. **Sortie déterministe.** À score égal, les résultats sont triés par
   identifiant. Deux exécutions sur les mêmes données donnent la même sortie,
   à l'octet près.
4. **Aucune dépendance à l'exécution.** La bibliothèque standard suffit. Une
   dépendance de développement (outil de test, de mesure) est acceptable si
   elle est justifiée.
5. **L'API publique** est ce qu'exporte `indexeur/__init__.py` : `Index`,
   `rechercher`, `Resultat`. Le reste peut changer.

## Tests

`tests/` contient un fichier de tests par module. Les tests n'utilisent ni le
réseau ni l'horloge, et les seuls fichiers qu'ils lisent sont ceux
d'`exemples/`.

## Banc d'essai

`bancs/banc_indexation.py` mesure l'indexation et la recherche sur un corpus
synthétique reproductible (`corpus.synthetique`, graine fixe).
