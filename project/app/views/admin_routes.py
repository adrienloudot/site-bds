#Routes pour l'interface admin

from flask import Blueprint, render_template
from ..models import User

bp = Blueprint('admin_routes', __name__, url_prefix='/admin')

@bp.route('/')
def admin_dashboard():
    users = User.query.all()
    return render_template('admin.html', users=users)
