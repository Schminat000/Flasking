import sys, os, logging, shutil, datetime
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_talisman import Talisman

db = SQLAlchemy()
DB_NAME = "flasking.db"

def create_app():
    app = Flask(__name__)
    talisman = Talisman(
    app,
    content_security_policy={
        "default-src": "'self'",
        "script-src": [
            "'self'",
            "'unsafe-inline'",
            "https://code.jquery.com",
            "https://cdnjs.cloudflare.com",
            "https://maxcdn.bootstrapcdn.com",
        ],
        "style-src": [
            "'self'",
            "https://stackpath.bootstrapcdn.com",
        ],
    },
    force_https=True
    )
    app.config["SECRET_KEY"] = "5ecret!"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_COOKIE_SECURE"] = True
    db.init_app(app)

    configure_logging(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def configure_logging(app):
    logging.basicConfig(format="[%(asctime)s] %(levelname)s %(name)s: %(message)s")
    logging.getLogger().setLevel(logging.INFO)

    if app.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    log_file_path = os.path.join(app.root_path, "logs", "app.log")
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    file_handler = RotatingFileHandler(log_file_path, maxBytes=1024 * 1024 * 10, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logging.getLogger().addHandler(file_handler)

    print("Log file path:", log_file_path)

def log_server_shutdown(signum, frame, app):
    try:
        backup_folder = os.path.join(app.instance_path, "database_backups")
        os.makedirs(backup_folder, exist_ok=True)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        db_path = os.path.join(app.instance_path, "flasking.db")
        backup_file = os.path.join(backup_folder, f"flasking_backup_{current_time}.db")
        shutil.copyfile(db_path, backup_file)
        logging.info("Server is shutting down...")
    
    except Exception as e:
        logging.error(F"Error during server shutdown: {e}")

    sys.exit(0)

def create_database(app):
    with app.app_context():
        db.create_all()
        logging.info("Database configured!")

def restore_database_from_backup(app, backup_folder):
    backup_files = os.listdir(backup_folder)
    if not backup_files:
        logging.info("No backup files found.")
        return False

    try:
        latest_backup = max(backup_files, key=lambda f: os.path.getmtime(os.path.join(backup_folder, f)))
        backup_file_path = os.path.join(backup_folder, latest_backup)
        original_db_path = os.path.join(app.instance_path, "flasking.db")

        shutil.copyfile(backup_file_path, original_db_path)
        
        logging.info(f"Database successfully restored from backup: {latest_backup}")
        return True
    except Exception as e:
        logging.error(f"Error restoring database from backup: {e}")
        return False
    
def perform_backup_or_restore(app):
    backup_folder = os.path.join("instance", "database_backups")
    db_file_path = os.path.join("instance", "flasking.db")

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    if not os.path.exists(db_file_path):
        if not os.listdir(backup_folder):
            create_database(app)
            logging.info("Created a new database.")
            return False
        else:
            if not restore_database_from_backup(app, backup_folder):
                logging.info("Failed to restore database from backup.")
                return False
    else:
        logging.info("Database file found. No backup needed.")
    
    return True