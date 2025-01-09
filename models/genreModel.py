from db import db
from models.livreGenreModel import livres_genres

class GenreModel(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False, unique=True)

    livres = db.relationship("LivreModel", secondary=livres_genres, back_populates="genres")