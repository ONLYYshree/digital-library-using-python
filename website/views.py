from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Ticket
views=Blueprint('views',__name__)

@views.route('/')
def base():
    return render_template("base.html")

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html",user=current_user)

@views.route('/ca')
def ca():
    return render_template('ca.html')

@views.route('/dmgt')
def dmgt():
    return render_template('dmgt.html')

@views.route('/dsa')
def dsa():
    return render_template('dsa.html')

@views.route('/eeim')
def eeim():
    return render_template('eeim.html')

@views.route('/helpdesk')
def helpdesk():
    return render_template('helpdesk.html', user=current_user)

@views.route('/helpdesk/submit', methods=['GET', 'POST'])
def submit_helpdesk():
    name = request.form.get('name')
    email = request.form.get('email')
    description = request.form.get('description')
    
    new_ticket = Ticket(user_id=current_user.id, category='Helpdesk', description=description)
    db.session.add(new_ticket)
    db.session.commit()

    flash('Your helpdesk request has been submitted!', category='success')
    return redirect(url_for('views.helpdesk'))

