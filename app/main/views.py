from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_quotes

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title="Le Blunt"
    randomquotes = get_quotes()

    return render_template('index.html', title=title, randomquotes = randomquotes)