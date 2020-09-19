from flask import Blueprint, render_template, request

import cs235flix.utilities.utilities as utilities

movie_blueprint = Blueprint('movie_bp', __name__)


@movie_blueprint.route('/movie')
def load_movie():
    temp_title = request.args.get('title')
    temp_date = request.args.get('date')
    return render_template('movies/movies.html', movie=utilities.get_movie_from_title(str(temp_title), int(temp_date)))



