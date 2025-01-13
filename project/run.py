from flask import request, render_template
from app.models import User, CertificatMedical, ReservationVan, CompetitionSportive, Calendrier
from app import create_app, db
import os
from flask_mail import Mail, Message    # pip install Flask-Mail
from app.views.user_routes import bp  # Importer le blueprint


# Fonction de récupération de la demande de réservation de van
@bp.route('/Van_page2.html')
def greet_van():

    #nom= email_glob
    nom = request.args.get('nom', '')

    association = request.args.get('association', '')
    date_début = request.args.get('date_début', '')
    date_fin = request.args.get('date_fin', '')
    #heure_début = request.args.get('heure_début', '')
    #heure_fin = request.args.get('heure_fin', '')
    remarque = request.args.get('remarque', '')

    if nom == '':
        msg = "Vous n'avez pas donné votre nom"
    else:
        msg = "Je suis " + nom + " et j'aimerais réserver un van de " + date_début + " à " + date_fin + ", pour l'association " + association
    if remarque != '':
        msg2 = remarque
    else:
        msg2 = "Il n'y a pas de remarque particulière"

    if nom != '':
        reservation = ReservationVan(nom_prenom=nom,
                                     heure_depart=date_début,
                                     heure_arrivee=date_fin,
                                     association=association,
                                     couleur_van='')

##comment faire pour transmettre à la bdd?
    try:
        db.session.add(reservation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Erreur lors de l'ajout à la base de données : {e}")

    send_email(nom, msg, msg2)
    return render_template('Van_page2.html', nom=nom, msg=msg, msg2=msg2)



# Fonction de récupération de la demande de réservation d'évènement
@bp.route('/Event_page2.html')
def greet_event():

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



# Configure l'envoie des mails
app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USE_SSL=False,
        MAIL_USERNAME="bdsenpc0@gmail.com",
        MAIL_PASSWORD="agjw khqp ittb nkxx"
    )
mail = Mail(app)  # Associer Flask-Mail à l'application
full_message=''

# Fonction d'envoie de mail (utilisée dans la fonction greet)
def send_email(nom, msg, msg2):
    email_content = render_template('Van_envoie_mail.html', nom=nom, msg=msg, msg2=msg2)
    msg = Message(subject= "Demande d'emprunt de van",
                  sender="bdsenpc0@gmail.com",
                  recipients=["teulon99@gmail.com"],
                  html=email_content)
    with app.app_context():
        mail.send(msg)
    print("Email envoyé")






with app.app_context():
    db.create_all()  # Crée les tables si elles n'existent pas encore 

if __name__ == '__main__':
    # Lancer l'application
    app.run(host='0.0.0.0', port=5000, debug= True)