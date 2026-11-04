# Programmation assistée par l'IA

*Discipline et outils pour le développement avec agents.* Cours de la TÉLUQ
(programme court de 1er cycle en développement logiciel assisté par l'IA).
Professeur responsable : Daniel Lemire.

Site du cours : <https://lemire.github.io/cours-programmation-ia/>

## Structure

| Dossier | Contenu |
|---|---|
| `index.qmd`, `mise-en-route.qmd`, `modules/` | le site du cours (livre Quarto, une page par semaine) |
| `evaluation.qmd` | les cinq travaux notés |
| `depot-exercice/` | **indexeur**, le dépôt d'exercice; publié sur le site en `indexeur.zip` |
| `outils/` | scripts de construction (archive du dépôt d'exercice) |
| `.github/workflows/publier.yml` | construction et publication sur GitHub Pages |

Le cours est découpé en quatre blocs : formuler (semaines 1 à 4), vérifier
(5 à 7), mesurer (8 à 10), outiller et orchestrer (11 à 15).

## Commandes

```bash
quarto preview                      # le site, avec rechargement
quarto render                       # le site complet dans _site/, avec indexeur.zip
cd depot-exercice && uv run pytest  # les tests du dépôt d'exercice
```

Chaque poussée sur `main` reconstruit et publie le site (GitHub Actions).
Le dépôt d'exercice doit rester tel que les personnes étudiantes le reçoivent
au départ : ses défauts (indexation quadratique, tests incomplets) sont
voulus et servent aux activités.
