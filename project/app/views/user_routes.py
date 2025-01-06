#Routes pour l'interface admin

from flask import Blueprint, render_template, request
from ..models import User, CertificatMedical, ReservationVan, CompetitionSportive, Calendrier
from datetime import datetime
from .. import db

bp = Blueprint('user_routes', __name__, url_prefix='/')


@bp.route('/test_db') #test d'affichage
def test_db():
    
    user_test = User(id= 1528,
                    username="ManyLaMélo",
                    email="bds@enpc.fr",
                    password="motdepasse",
                    is_admin= True)


    db.session.add(user_test)
    db.session.commit()    

    users = User.query.all()  # Récupère tous les utilisateurs
    return "<br>".join([f"ID: {user.id}, Username: {user.username}" for user in users])

@bp.route('/')
def index():
   return render_template('Accueil.html')

@bp.route('/Accueil.html')
def Accueil():
    return render_template('Accueil.html')

@bp.route('/Mandats.html')
def organigramme():
    return render_template('Mandats.html')

@bp.route('/Partenaires.html')
def partenaires():
    return render_template('Partenaires.html')

@bp.route('/Les sports aux ponts.html')
def sports():
    return render_template('Les sports aux ponts.html')
@bp.route('/club/Pompims.html')
def Pompims():
    return render_template('/club/Pompims.html')
@bp.route('/club/Course.html')
def Course():
    return render_template('/club/Course.html')
@bp.route('/club/Escalade.html')
def Escalade():
    return render_template('/club/Escalade.html')
@bp.route('/club/Aviron.html')
def Aviron():
    return render_template('/club/Aviron.html')
@bp.route('/club/Rock.html')
def Rock():
    return render_template('/club/Rock.html')
@bp.route('/club/Voile.html')
def Voile():
    return render_template('/club/Voile.html')
@bp.route('/club/Micro Aventure.html')
def MicroAventure():
    return render_template('/club/Micro Aventure.html')
@bp.route('/club/Ultra.html')
def Ultra():
    return render_template('/club/Ultra.html')
@bp.route('/club/Rugbyx.html')
def Rugbyx():
    return render_template('/club/Rugbyx.html')
@bp.route('/Contacts.html')
def contacts():
    return render_template('Contacts.html')

@bp.route('/Van.html')
def home():
    return render_template('Van.html')

@bp.route('/Event.html')  # Définir la route pour Event.html
def event_page():
    return render_template('Event.html')