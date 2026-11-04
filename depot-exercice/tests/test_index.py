import pytest

from indexeur.index import Index


def test_index_vide():
    index = Index()
    assert len(index) == 0
    assert index.documents_avec("chat") == []
    assert index.longueur_moyenne() == 0.0


def test_ajouter_et_retrouver():
    index = Index()
    index.ajouter("a", "le chat dort")
    index.ajouter("b", "le chien et le chat jouent")
    assert len(index) == 2
    assert "a" in index
    assert index.documents_avec("chat") == ["a", "b"]
    assert index.documents_avec("chien") == ["b"]


def test_frequences():
    index = Index()
    index.ajouter("a", "chat chat chien")
    assert index.frequence("chat", "a") == 2
    assert index.frequence("chien", "a") == 1
    assert index.frequence("souris", "a") == 0


def test_longueur_moyenne():
    index = Index()
    index.ajouter("a", "chat chien")  # 2 termes
    index.ajouter("b", "chat chien souris loup")  # 4 termes
    assert index.longueur_moyenne() == 3.0


def test_identifiant_en_double_refuse():
    index = Index()
    index.ajouter("a", "chat")
    with pytest.raises(ValueError):
        index.ajouter("a", "chien")
