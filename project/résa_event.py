from flask import request, render_template
from app.models import User, CertificatMedical, ReservationVan, CompetitionSportive, Calendrier
from app import create_app, db
import os
from flask_mail import Mail, Message    # pip install Flask-Mail
from app.views.user_routes import bp  # Importer le blueprint


@bp.route('/Event.html')  # Définir la route pour Event.html
def event_page():
    return render_template('Event.html')


# Fonction de récupération de la demande de réservation d'évènement
@bp.route('/Event_page2.html')
def greet():

    nom = request.args.get('nom', '')
    event = request.args.get('event', '')
    remarque = request.args.get('remarque', '')

    if nom == '':
        msg = "Vous n'avez pas donné votre nom"
    else:
        msg = "Je suis " + nom + " et j'aimerais participer à l'évènement " + event
    if remarque != '':
        msg2 = remarque
    else:
        msg2 = "Il n'y a pas de remarque particulière"

    if nom != '':
        reservation = CompetitionSportive(nom_prenom=nom,
                                          competition=event,
                                          remarques=remarque
                                          )

##comment faire pour transmettre à la bdd?
    try:
        db.session.add(reservation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Erreur lors de l'ajout à la base de données : {e}")

    return render_template('Event_page2.html', nom=nom, msg=msg, msg2=msg2)



# Créer une instance de l'application
app = create_app()




with app.app_context():
    db.create_all()  # Crée les tables si elles n'existent pas encore 

if __name__ == '__main__':
    # Lancer l'application
    app.run(host='0.0.0.0', port=5000, debug= True)


