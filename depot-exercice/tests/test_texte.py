from indexeur.texte import normaliser, sans_accents, termes


def test_sans_accents():
    assert sans_accents("Élève à l'été") == "Eleve a l'ete"


def test_normaliser_minuscules_et_ligatures():
    assert normaliser("Œuvre") == "oeuvre"
    assert normaliser("CŒUR") == "coeur"


def test_termes_retire_les_mots_vides():
    assert termes("Le chat et la souris") == ["chat", "souris"]


def test_termes_retire_les_nombres():
    assert termes("3 pommes et 12 poires") == ["pommes", "poires"]


def test_termes_apostrophes():
    assert termes("L'école d'été") == ["ecole"]


def test_termes_texte_vide():
    assert termes("") == []
