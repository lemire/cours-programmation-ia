"""Après le rendu du site : met le dépôt d'exercice dans une archive zip
téléchargeable, _site/indexeur.zip (le dépôt du cours n'est pas public)."""

import os
import zipfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SOURCE = RACINE / "depot-exercice"
SORTIE = RACINE / os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site") / "indexeur.zip"
IGNORES = {"__pycache__", ".venv", ".pytest_cache", ".DS_Store"}

SORTIE.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(SORTIE, "w", zipfile.ZIP_DEFLATED) as archive:
    for chemin in sorted(SOURCE.rglob("*")):
        relatif = chemin.relative_to(SOURCE)
        if chemin.is_file() and not IGNORES.intersection(relatif.parts):
            archive.write(chemin, Path("indexeur") / relatif)
print(f"archive : {SORTIE.relative_to(RACINE)}")
