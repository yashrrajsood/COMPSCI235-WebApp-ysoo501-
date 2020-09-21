from flask import Blueprint, render_template, request

import cs235flix.utilities.utilities as utilities

director_blueprint = Blueprint('director_bp', __name__)


@director_blueprint.route('/directors')
def get_list_of_directors():
    return render_template('director/director.html', director_list=utilities.get_list_of_directors())


@director_blueprint.route('/director_movies')
def get_director_movies():
    name = request.args.get('director')
    return render_template('director/director_display.html', list_movies=utilities.get_movies_by_director(name), director_name=name)

