from pathlib import Path

from indexeur.cli import main

EXEMPLES = Path(__file__).parent.parent / "exemples"


def test_chercher(capsys):
    assert main(["chercher", str(EXEMPLES), "érable"]) == 0
    sortie = capsys.readouterr().out
    assert "erabliere.txt" in sortie


def test_stats(capsys):
    assert main(["stats", str(EXEMPLES)]) == 0
    sortie = capsys.readouterr().out
    assert "documents : 6" in sortie
