from flask import Blueprint, render_template, request

import cs235flix.utilities.utilities as utilities

home_blueprint = Blueprint(
    'home_bp', __name__, url_prefix='/home')


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        all_movies=utilities.get_movies_by_rank(),
        genre_list=utilities.get_list_of_genres()
    )


@home_blueprint.route('/all_movies', methods=['GET'])
def all_movies():
    return render_template('home/all_movies.html', all_movies=utilities.get_movies_by_rank())
