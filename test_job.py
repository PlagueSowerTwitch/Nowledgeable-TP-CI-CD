import pytest
from job import moyenne
from job import moyenne_erreur

class TestMoyenne:
    def test_moyenne_simple(self):
        """Test avec une liste simple"""
        assert moyenne([1, 2, 3]) == 2
    
    def test_moyenne_nombres_decim(self):
        """Test avec des nombres décimaux"""
        assert moyenne([1.5, 2.5, 3.5]) == 2.5
    
    def test_moyenne_nombres_negatifs(self):
        """Test avec des nombres négatifs"""
        assert moyenne([-1, 0, 1]) == 0
    
    def test_moyenne_exemple(self):
        """Test avec l'exemple du fichier"""
        assert moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
    
    def test_moyenne_un_seul_element(self):
        """Test avec un seul élément"""
        assert moyenne([5]) == 5
    
    def test_moyenne_nombres_identiques(self):
        """Test avec des nombres identiques"""
        assert moyenne([7, 7, 7, 7]) == 7

class TestMoyenneErreur:
    def test_moyenne_simple_erreur(self):
        """Test avec une liste simple"""
        assert moyenne_erreur([1, 2, 3]) == 2
    
    def test_moyenne_nombres_decim_erreur(self):
        """Test avec des nombres décimaux"""
        assert moyenne_erreur([1.5, 2.5, 3.5]) == 2.5
    
    def test_moyenne_nombres_negatifs_erreur(self):
        """Test avec des nombres négatifs"""
        assert moyenne_erreur([-1, 0, 1]) == 0
    
    def test_moyenne_exemple_erreur(self):
        """Test avec l'exemple du fichier"""
        assert moyenne_erreur([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
    
    def test_moyenne_un_seul_element_erreur(self):
        """Test avec un seul élément"""
        assert moyenne_erreur([5]) == 5

    def test_moyenne_nombres_identiques_erreur(self):
        """Test avec des nombres identiques"""
        assert moyenne_erreur([7, 7, 7, 7]) == 7
