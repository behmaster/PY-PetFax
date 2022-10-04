from flask import ( Blueprint, redirect, render_template, request, redirect )
from . import models

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        fact = request.form['fact']

        new_fact = models.Fact(author=author,title=title,fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        # print(request.form)
        return redirect('/facts')
    results = models.Fact.query.all()

    return render_template('facts/index.html', facts=results)
    # return "Thanks for submitting a fun fact about pets!"

@bp.route('/new')
def new_fact():
    return render_template('facts/new.html')