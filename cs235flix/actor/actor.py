from flask import Blueprint, render_template, request

import cs235flix.utilities.utilities as utilities

actor_blueprint = Blueprint('actor_bp', __name__)


@actor_blueprint.route('/actors')
def get_list_of_genres():
    return render_template('actor/actor.html', actor_list=utilities.get_list_of_actors())


@actor_blueprint.route('/actor_movies')
def get_actor_movies():
    name = request.args.get('actor')
    return render_template('actor/actor_display.html', list_movies=utilities.get_movies_by_actor(name), actor_name=name)

