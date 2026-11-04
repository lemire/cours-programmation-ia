"""indexeur : un petit moteur de recherche plein texte."""

from indexeur.index import Index
from indexeur.recherche import Resultat, rechercher

__all__ = ["Index", "Resultat", "rechercher"]
__version__ = "0.3.0"
