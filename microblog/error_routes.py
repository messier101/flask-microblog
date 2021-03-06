from flask import render_template
from microblog import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal(error):
    db.session.rollback()
    return render_template('500.html'), 500
