from flask import Blueprint, render_template, request, session, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError


from werkzeug.utils import redirect
import cs235flix.utilities.utilities as utilities
from cs235flix.authentication.authentication import login_required

movie_blueprint = Blueprint('movie_bp', __name__)


@movie_blueprint.route('/movie')
def load_movie():
    user_watchlist = load_user_and_watchlist()
    temp_title = request.args.get('title')
    temp_date = int(request.args.get('date'))
    return render_template('movies/movies.html'
                           , movie=utilities.get_movie_from_title(str(temp_title), int(temp_date))
                           , user_watchlist=user_watchlist
                           , movie_reviews=utilities.get_reviews_for_movie(temp_title, temp_date)
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


@movie_blueprint.route("/review", methods=['GET', 'POST'])
@login_required
def add_review():
    username = utilities.get_user(str(session['username']))
    form = ReviewForm()
    if form.validate_on_submit():
        movie_title = str(form.movie.data)
        movie_date = form.movie_date.data
        utilities.add_review(str(session['username']), form.review_text.data, movie_title, movie_date, form.rating.data)
        return redirect(url_for('movie_bp.load_movie', title=movie_title, date=movie_date))

    if request.method == 'GET':
        movie_title = request.args.get('movie_title')
        movie_date = request.args.get('movie_date')
        form.movie.data = movie_title

        form.movie_date.data = movie_date
    else:
        movie_title = str(form.movie.data)
        movie_date = form.movie_date.data

    return render_template(
        'movies/review_on_movie.html',
        title='Review Movie',
        movie_title=movie_title,
        movie_date=movie_date,
        form=form,
        handler_url=url_for('movie_bp.add_review'),
        username=username
    )


class ReviewForm(FlaskForm):
    """Review form."""
    review_text = StringField('Review Text', [DataRequired()])
    rating = StringField('Rating (1-10)', [DataRequired()])
    movie = HiddenField("Movie Name")
    movie_date = HiddenField("Movie Date")
    username = HiddenField("username")
    submit = SubmitField('Submit')
