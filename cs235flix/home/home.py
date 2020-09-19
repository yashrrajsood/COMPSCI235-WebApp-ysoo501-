from flask import Blueprint, render_template, request

import cs235flix.utilities.utilities as utilities


home_blueprint = Blueprint(
    'home_bp', __name__, url_prefix='/home')


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        all_movies=utilities.get_movies_by_rank()
    )
