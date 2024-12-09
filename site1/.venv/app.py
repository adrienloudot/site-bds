from flask import Flask,render_template, send_from_directory, request
from flask_mail import Mail, Message    # pip install Flask-Mail
import os

app=Flask(__name__)

@app.route('/')
def index():
   return render_template('Accueil.html')




@app.route('/Accueil.html')
def Accueil():
    return render_template('Accueil.html')

@app.route('/Mandats.html')
def organigramme():
    return render_template('Mandats.html')

@app.route('/Partenaires.html')
def partenaires():
    return render_template('Partenaires.html')

@app.route('/Les sports aux ponts.html')
def sports():
    return render_template('Les sports aux ponts.html')
@app.route('/club/Pompims.html')
def Pompims():
    return render_template('/club/Pompims.html')
@app.route('/club/Course.html')
def Course():
    return render_template('/club/Course.html')
@app.route('/club/Escalade.html')
def Escalade():
    return render_template('/club/Escalade.html')
@app.route('/club/Aviron.html')
def Aviron():
    return render_template('/club/Aviron.html')
@app.route('/club/Rock.html')
def Rock():
    return render_template('/club/Rock.html')
@app.route('/club/Voile.html')
def Voile():
    return render_template('/club/Voile.html')
@app.route('/club/Micro Aventure.html')
def MicroAventure():
    return render_template('/club/Micro Aventure.html')
@app.route('/club/Ultra.html')
def Ultra():
    return render_template('/club/Ultra.html')
@app.route('/club/Rugbyx.html')
def Rugbyx():
    return render_template('/club/Rugbyx.html')


@app.route('/Contacts.html')
def contacts():
    return render_template('Contacts.html')


@app.route('/Van.html')
def home():
    return render_template('Van.html')


mail_settings = {
     "MAIL_SERVER": 'smtp.gmail.com',
     "MAIL_PORT": 587,
     "MAIL_USE_TLS": True,
     "MAIL_USE_SSL": False,
     "MAIL_USERNAME": "bdsenpc0@gmail.com",
     "MAIL_PASSWORD": "agjw khqp ittb nkxx"
}

app.config.update(mail_settings)
mail = Mail(app)

full_message=''
@app.route('/Van_page2.html')
def greet():
    nom = request.args.get('nom', '')

    association = request.args.get('association', '')

    date_début = request.args.get('date_début', '')

    date_fin = request.args.get('date_fin', '')

    heure_début = request.args.get('heure_début', '')

    heure_fin = request.args.get('heure_fin', '')

    remarque = request.args.get('remarque', '')

    if nom == '':
        msg = "Vous n'avez pas donné votre nom"

    else:
        msg = "Je suis " + nom + " et j'aimerai réserver un van de " + date_début + " à " + date_fin + ", pour l'association " + association

    if remarque != '':
        msg2 = remarque

    else:
        msg2 = "Il n'y a pas de remarque particulière"

    send_email(nom, msg, msg2)
    return render_template('Van_page2.html').format(nom, msg, msg2)


def send_email(nom, msg, msg2):
    email_content = render_template('Van_envoie_mail.html', nom=nom, msg=msg, msg2=msg2)
    
    msg = Message(subject= "Demande d'emprunt de van",
                  sender="bdsenpc0@gmail.com",
                  recipients=["teulon99@gmail.com"],
                  html=email_content)

    with app.app_context():
        mail.send(msg)

    print("Email envoyé")


if __name__=="__main__":
   app.run(host="0.0.0.0", port=5000, debug=True)

#172.29.5.125