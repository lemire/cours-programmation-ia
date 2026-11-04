from indexeur.index import Index
from indexeur.recherche import intersection, rechercher


def petit_index():
    index = Index()
    index.ajouter("a", "Le chat dort sur le canapé.")
    index.ajouter("b", "Le chat et le chien jouent dans le jardin.")
    index.ajouter("c", "Le chien aboie. Le chien court. Le chien dort.")
    index.ajouter("d", "Une souris traverse la cuisine.")
    return index


def test_intersection():
    assert intersection([[1, 2, 3], [3, 2], [2, 3, 4]]) == [2, 3]
    assert intersection([[1, 2]]) == [1, 2]
    assert intersection([]) == []


def test_un_terme():
    ids = [r.identifiant for r in rechercher(petit_index(), "chat")]
    assert sorted(ids) == ["a", "b"]


def test_tous_les_termes_requis():
    ids = [r.identifiant for r in rechercher(petit_index(), "chat chien")]
    assert ids == ["b"]


def test_classement_par_frequence():
    resultats = rechercher(petit_index(), "chien")
    assert resultats[0].identifiant == "c"
    assert resultats[0].score > resultats[1].score


def test_insensible_aux_accents_et_a_la_casse():
    ids = [r.identifiant for r in rechercher(petit_index(), "CANAPE")]
    assert ids == ["a"]


def test_aucun_resultat():
    assert rechercher(petit_index(), "girafe") == []
    assert rechercher(petit_index(), "le la les") == []


def test_k_limite_le_nombre_de_resultats():
    assert len(rechercher(petit_index(), "dort", k=1)) == 1
