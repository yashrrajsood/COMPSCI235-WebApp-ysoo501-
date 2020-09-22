from flask import Blueprint, render_template, request

import cs235flix.utilities.utilities as utilities

watchlist_blueprint = Blueprint('watchlist_bp', __name__)


@watchlist_blueprint.route('/watchlist')
def get_user_watchlist():
    temp_watchlist = utilities.get_user_watchlist(str(temp_user))
    temp_user = temp_watchlist.get_owner()
    return render_template('watchlist/watchlist.html', watchlist=temp_watchlist, user=temp_user)



