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
        event_request = EventRequest(**request_data)  # Raises ValidationError if invalid
    except ValidationError as e:
        logging.error(e.errors())
        return jsonify(error=f"Invalid request body: {e.errors()}"), 400

    try:
        # Process events and retrieve data
        processed_events = await process_events(event_request)
        #TODO: change .dict() to model_dump() and test
        processed_events_dict = [event.dict() for event in processed_events]
        return jsonify(processed_events_dict)
    except Exception as e:
        logging.error(f"Internal Server Error: {e}", exc_info=True)
        return jsonify(error=f"Internal Server Error: {str(e)}"), 500
        