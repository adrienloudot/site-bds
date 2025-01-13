#Classe de données 

from . import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  #Mot de passe haché ==> utiliser des bibliothèques
    is_admin = db.Column(db.Boolean, default=False)

    #site officiel pour mieux définir les classes

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    

class CertificatMedical(db.Model):
    __tablename__ = 'certificat_medical'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_prenom = db.Column(db.String(255), nullable=False, unique=True)
    pdf_path = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<CertificatMedical {self.nom_prenom}>"

class ReservationVan(db.Model):
    __tablename__ = 'reservation_van'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_prenom = db.Column(db.String(255), nullable=False)
    heure_depart = db.Column(db.String(255), nullable=False)
    heure_arrivee = db.Column(db.String(255), nullable=False)
    association = db.Column(db.String(255), nullable=True)
    couleur_van = db.Column(db.String(50), nullable=True)
    statut = db.Column(db.String(50), nullable=False, default="en attente")

    def __repr__(self):
        return f"<ReservationVan {self.nom_prenom} - {self.statut}>"

class CompetitionSportive(db.Model):
    __tablename__ = 'competition_sportive'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom_prenom = db.Column(db.String(255), nullable=False)
    competition = db.Column(db.String(255), nullable=False)
    remarques = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<CompetitionSportive {self.nom_prenom} - {self.competition}>"

class Calendrier(db.Model):
    __tablename__ = 'calendrier'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jour = db.Column(db.Date, nullable=False)
    heure = db.Column(db.Time, nullable=False)
    evenement = db.Column(db.String(255), nullable=False)
    etat_vans = db.Column(db.String(255), nullable=True)  # Exemple: "bleu:dispo, jaune:occupé, blanc:dispo"

    def __repr__(self):
        return f"<Calendrier {self.jour} - {self.heure} - {self.evenement}>"

