from flask import Blueprint, render_template, request, abort, redirect, url_for
from flask_login import login_required, current_user
from .models import Room
from . import db
from datetime import datetime

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    rooms = Room.query.all()
    return render_template('index.html', user=current_user, rooms=rooms)

@views.route('/create-room', methods=['GET', 'POST'])
def create_room():
    if request.method == 'POST':
        name = request.form.get('roomName')
        datetime_obj = datetime.now()
        created_at = datetime_obj.date()

        new_room = Room(name=name, created_at=created_at)
        db.session.add(new_room)
        db.session.commit()

        return redirect(url_for('views.home'))
    return render_template('index.html')