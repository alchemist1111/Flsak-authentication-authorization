from flask import Flask # type: ignore
from extensions import db, jwt
from auth import auth_bp
from users import user_bp

def create_app():
    app = Flask(__name__)
    
    app.config.from_prefixed_env()
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    #Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/all')
    
    
    return app