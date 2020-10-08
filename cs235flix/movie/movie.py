from flask import Blueprint, render_template, request, session, url_for
from werkzeug.utils import redirect

import cs235flix.utilities.utilities as utilities
from cs235flix.authentication.authentication import login_required

movie_blueprint = Blueprint('movie_bp', __name__)


@movie_blueprint.route('/movie')
def load_movie():
    user_watchlist = load_user_and_watchlist()
    temp_title = request.args.get('title')
    temp_date = request.args.get('date')
    return render_template('movies/movies.html'
                           , movie=utilities.get_movie_from_title(str(temp_title), int(temp_date))
                           , user_watchlist=user_watchlist
                           )


@movie_blueprint.route("/add_to_watchlist/")
@login_required
def add_movie_to_watchlist():
    user_watchlist = load_user_and_watchlist()
    user = str(session['username'])
    movie = request.args.get('title')
    date = request.args.get('date')
    utilities.add_movie_to_watchlist(user, movie, date)

    return redirect(request.referrer)


@movie_blueprint.route("/removed_from_watchlist/")
@login_required
def remove_movie_from_watchlist():
    user_watchlist = load_user_and_watchlist()
    user = str(session['username'])
    movie = request.args.get('title')
    date = request.args.get('date')
    utilities.remove_movie_from_watchlist(user, movie, date)

    return redirect(request.referrer)


def load_user_and_watchlist():
    temp_user = None
    user_watchlist = None
    if 'username' in session:
        temp_user = utilities.get_user(str(session['username']))
        user_watchlist = utilities.get_user_watchlist(str(session['username']))
    return user_watchlist
