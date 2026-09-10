from abc import ABC,abstractmethod
from datetime import date


class Employe(ABC):
    
    def __init__(self,nom,prenom,date_naissance,matricule):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.matricule = matricule
    
    def __str__(self):
        return f"{self.nom} {self.prenom} {self.date_naissance} {self.matricule} "
    
    @abstractmethod
    def get_salaire(self):
        pass
    


class Ouvrier(Employe):
    
    SMIG = 2500
    
    def __init__(self, nom, prenom, date_naissance, matricule,salaire,annee_entree):
        super().__init__(nom, prenom, date_naissance, matricule)
        self.annee_entree = annee_entree
        
    def get_salaire(self):
        annee = date.today().year
        salaiire = self.SMIG + ((annee - self.annee_entree  ) * 100)
        
        return min(salaiire,self.SMIG * 2)
    
    def __str__(self):
        return f"{super().__str__()} "
        
        
class Cadre(Employe):
    
    def __init__(self, nom, prenom, date_naissance, matricule):
        super().__init__(nom, prenom, date_naissance, matricule)
        
    def get_salaire(self):
        return self.salaire
    
    def __str__(self):
        return f"{super().__str__()}"
    
    
class patron(Employe):
    
    def __init__(self, nom, prenom, date_naissance, matricule):
        super().__init__(nom, prenom, date_naissance, matricule)
    
        
    def get_salaire(self):
        return self.salaire
    
    
    def __str__(self):
        return f"{super().__str__()}"