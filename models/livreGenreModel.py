from db import db

livres_genres = db.Table(
    'livres_genres',
    db.Column('livre_id', db.Integer, db.ForeignKey('livres.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)