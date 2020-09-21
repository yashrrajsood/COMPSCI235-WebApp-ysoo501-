from flask import Blueprint, render_template, request

import cs235flix.utilities.utilities as utilities

genre_blueprint = Blueprint('genre_bp', __name__)


@genre_blueprint.route('/genre')
def get_list_of_genres():
    return render_template('genre/genre.html', genre_list=utilities.get_list_of_genres())


@genre_blueprint.route('/genre_movie')
def get_genre_movies():
    name = request.args.get('genre')
    return render_template('genre/genre_movie.html', list_movies=utilities.get_movies_by_genre(name), genre_name=name)

