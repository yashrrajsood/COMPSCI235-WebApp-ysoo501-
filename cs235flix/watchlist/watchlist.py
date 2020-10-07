from flask import Blueprint, render_template, session

import cs235flix.utilities.utilities as utilities


watchlist_blueprint = Blueprint('watchlist_bp', __name__)


@watchlist_blueprint.route('/watchlist')
def get_user_watchlist():
    username = str(session['username'])
    user_watchlist = utilities.get_user_watchlist(username)
    if user_watchlist == None:
        watchlist_len = 0
    else:
        watchlist_len = len(user_watchlist)
    temp_user = utilities.get_user(username)
    return render_template('watchlist/watchlist.html'
                           , watchlist=user_watchlist
                           , watchlist_len=watchlist_len
                           , user=temp_user
                           )



