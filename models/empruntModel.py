from db import db

class EmpruntModel(db.Model):
    __tablename__ = "emprunts"

    id = db.Column(db.Integer, primary_key=True)
    date_debut = db.Column(db.Date, nullable=False)
    date_retour = db.Column(db.Date, nullable=True)
    adherent_id = db.Column(db.Integer, db.ForeignKey('adherents.id'), nullable=False)
    livre_id = db.Column(db.Integer, db.ForeignKey('livres.id'), nullable=False)
    retourner = db.Column(db.Boolean, default=False, nullable=False)
    
    adherent = db.relationship('AdherentModel', back_populates='emprunts')
    livre = db.relationship('LivreModel', back_populates='emprunts')