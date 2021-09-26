from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_quotes, get_quotes1, get_quotes2, get_quotes3, get_quotes4
from flask_login import login_required, current_user

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title="Le Blunt"
    randomquotes = get_quotes()
    randomquotes1 = get_quotes1()
    randomquotes2 = get_quotes2()
    randomquotes3 = get_quotes3()
    randomquotes4 = get_quotes4()

    return render_template('index.html', title=title, randomquotes = randomquotes, randomquotes1=randomquotes1, randomquotes2=randomquotes2, randomquotes3=randomquotes3, randomquotes4=randomquotes4)

@main.route('/userblogpage', methods = ['GET', 'POST'])
@login_required
def userblogpage():
    '''
    View userpage page function that returns the userpage page and its data
    ''' 

    return render_template('userblogpage.html')