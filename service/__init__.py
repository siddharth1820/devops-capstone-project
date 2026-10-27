
from flask import Flask
from flask_cors import CORS


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def index():
        return {
            "service": "Customer Accounts Microservice",
            "status": "running"
        }, 200

    return app


app = create_app()
