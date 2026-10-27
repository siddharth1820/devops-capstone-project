
from flask import Flask
from flask_cors import CORS

from service.routes import accounts_bp


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(accounts_bp)

    @app.route("/")
    def index():
        return {
            "service": "Customer Accounts Microservice",
            "status": "running"
        }, 200

    return app


app = create_app()
