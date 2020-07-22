from flask import render_template
from app import app

@app.route('/')
def index ():
    '''
    a view route function that returns the index.html and its data
    '''
    return render_template ('index.html')