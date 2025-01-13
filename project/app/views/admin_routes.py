#Routes pour l'interface admin
from ..models import User, ReservationVan, CompetitionSportive
from flask import Blueprint, request, jsonify, render_template
from app.extensions import db
from flask_jwt_extended import create_access_token

bp = Blueprint('admin_routes', __name__, url_prefix='/admin')


@bp.route('/')
def admin_dashboard():
    users = User.query.all()
    return render_template('admin.html', users=users)


@bp.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')  # Récupère les données du formulaire
        password = request.form.get('password')
        username = request.form.get('username')


        # Vérifier si l'utilisateur existe déjà
        if User.query.filter_by(email=email).first():
            return render_template('register.html', error="User already exists")

        # Créer un nouvel utilisateur
        new_user = User(email=email, username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return render_template('register.html', success="User registered successfully")

    return render_template('register.html')  # Affiche le formulaire d'inscription


@bp.route('/login.html', methods=['GET', 'POST'])
def login_dashboard():
    if request.method == 'POST':
        email = request.form.get('email')  # Récupère les données du formulaire
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            # Rediriger vers le tableau de bord ou une autre page en cas de succès
            résa = ReservationVan.query.filter_by(nom_prenom=email) 

            compet=CompetitionSportive.query.filter_by(nom_prenom=email) 
            
            

            #A faire: Afficher les demandes de résa van




            return render_template('dashboard.html', RéservationVans=résa, RéservationEvent=compet)
        


        # Afficher un message d'erreur en cas d'échec
        return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')  # Affiche le formulaire de connexion


@bp.route('/test', methods=['GET', 'POST'])
def test():
    return jsonify({'message': 'Test route works!'})

