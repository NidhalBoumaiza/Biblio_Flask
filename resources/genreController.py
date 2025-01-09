from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import GenreModel
from schemas import GenreSchema, GenreUpdateSchema

# Create a Blueprint for genres
blp = Blueprint("Genres", __name__, description="Operations on genres")


@blp.route("/genre/<int:genre_id>")
class Genre(MethodView):
    @blp.response(200, GenreSchema)
    def get(self, genre_id):
        """Get a genre by its ID."""
        genre = GenreModel.query.get_or_404(genre_id)
        return genre

    def delete(self, genre_id):
        """Delete a genre by its ID."""
        genre = GenreModel.query.get_or_404(genre_id)
        db.session.delete(genre)
        db.session.commit()
        return {"message": "Genre deleted."}

    @blp.arguments(GenreUpdateSchema)
    @blp.response(200, GenreSchema)
    def put(self, genre_data, genre_id):
        """Update a genre by its ID."""
        genre = GenreModel.query.get(genre_id)

        if genre:
            genre.name = genre_data["name"]
        else:
            genre = GenreModel(id=genre_id, **genre_data)

        db.session.add(genre)
        db.session.commit()

        return genre


@blp.route("/genre")
class GenreList(MethodView):
    @blp.response(200, GenreSchema(many=True))
    def get(self):
        """Get a list of all genres."""
        return GenreModel.query.all()

    @blp.arguments(GenreSchema)
    @blp.response(201, GenreSchema)
    def post(self, genre_data):
        """Create a new genre."""
        genre = GenreModel(**genre_data)

        try:
            db.session.add(genre)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the genre.")

        return genre
    

@blp.route("/genre/find/<string:name>")
class GenreByName(MethodView):
    @blp.response(200, GenreSchema)
    def get(self, name):
        """Find a genre by its name."""
        genre = GenreModel.query.filter_by(name=name).first()
        if not genre:
            abort(404, message=f"Genre with name '{name}' not found.")
        return genre