'''

from flask import Blueprint, render_template

import cs235flix.utilities.utilities as utilities

movie_blueprint = Blueprint('movie_bp', __name__)


@movie_blueprint.route('/movies_by_rank', methods=['GET'])
def movies_by_rank():
    return render_template('templates/movies/movie.html', movies_by_rank=utilities.get_movies_by_rank())


@movie_blueprint.route('/all_movies', methods=['GET'])
def all_movies():
    return render_template('templates/movies/movie.html', all_movies=utilities.get_movies())
'''