from flask import render_template, request, redirect, url_for, abort
from . import main
from ..requests import get_quotes, get_quotes1, get_quotes2, get_quotes3, get_quotes4
from flask_login import login_required, current_user
from ..models import User
from . forms import UpdateProfile
from ..import db, photos

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

#Display profile
@main.route('/user/<uname>')
def profile(uname):

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

#Update Profile

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def updateprofile(uname):

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template("profile/update.html", form = form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def updateppic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:

        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname=uname))

