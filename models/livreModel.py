from db import db
from models.livreGenreModel import livres_genres

class LivreModel(db.Model):
    __tablename__ = "livres"

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False, unique=True)
    nbre_pages = db.Column(db.Integer, nullable=False)
    code_auteur = db.Column(db.Integer, db.ForeignKey('auteurs.id'), nullable=False)
    disponible = db.Column(db.Boolean, default=True)
    nbre_exemplaires = db.Column(db.Integer, nullable=False, default=1)  # Nouveau champ
    
    genres = db.relationship("GenreModel", secondary=livres_genres, back_populates="livres")
    auteur = db.relationship('AuteurModel', back_populates='livres')
    emprunts = db.relationship('EmpruntModel', back_populates='livre')