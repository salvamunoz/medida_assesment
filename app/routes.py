from flask import request, jsonify, Blueprint
from pydantic import ValidationError
from .utils import process_events
from .models import EventRequest
import logging

bp = Blueprint('api', __name__)


@bp.route('/events', methods=['POST'])
async def polling_events():
    request_data = request.json
    
    try:
        # Validate request body
        EventRequest(**request_data)  # Raises ValidationError if invalid
    except ValidationError as e:
        return jsonify(error=f"Invalid request body: {e.errors()}"), 400

    try:
        # Process events and retrieve data
        processed_events = await process_events(request_data)
        return jsonify(processed_events)
    except Exception as e:
        logging.error(f"Internal Server Error: {e}", exc_info=True)
        return jsonify(error=f"Internal Server Error: {str(e)}"), 500
        