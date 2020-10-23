from werkzeug.utils import redirect
from wtforms import Form, StringField, SelectField
from flask import Blueprint, render_template, request, flash

import cs235flix.utilities.utilities as utilities

search_blueprint = Blueprint(
    'search_bp', __name__)


# endpoint for search
@search_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        book = request.form['book']
        # search by author or book
        list_of_movies = utilities.get_movies()
        data = []
        for movie in list_of_movies:
            if str(book).lower() in movie.director._name.lower() or book.lower() == movie.director._name.lower():
                data += [movie]
            for actor in movie.actors:
                if str(book).lower() in actor._name.lower() or book.lower() == actor._name.lower():
                    data += [movie]
            for genre in movie.genres:
                if str(book).lower() in genre._name.lower() or book.lower() == genre._name.lower():
                    data += [movie]
            if str(book).lower() in movie.title.lower() or str(book).lower() == movie.title.lower():
                data += [movie]
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all':
            data = utilities.get_movies()
        return render_template('search/search.html', data=data, datalen= len(data))
    return render_template('search/search.html')
