from flask import ( Blueprint, render_template )

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template('facts/index.html')

@bp.route('/new')
def new_fact():
    return render_template('facts/new.html')