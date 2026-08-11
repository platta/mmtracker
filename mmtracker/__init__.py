"""MMTracker application package."""

from flask import Flask


def create_app() -> Flask:
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        # Import pieces.
        from .hello import hello_blueprint

        # Register Blueprints.
        app.register_blueprint(hello_blueprint)

        return app
