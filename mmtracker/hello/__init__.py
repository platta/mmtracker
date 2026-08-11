"""Hello package."""

import os
from typing import Tuple

from flask import Blueprint, current_app, render_template, jsonify

# Name of blueprint.
BLUEPRINT_NAME = os.path.basename(os.path.dirname(__file__))

# Blueprint configuration.
hello_blueprint = Blueprint(BLUEPRINT_NAME, BLUEPRINT_NAME)


@hello_blueprint.route('/hello', methods=['GET'])
def hello() -> Tuple[str, int]:
    """Simple hello method."""
    return (
        jsonify({
            'message': 'success'
        }),
        200
    )
