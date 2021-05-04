from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
import sys

# write your code here
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
parser = reqparse.RequestParser()


class EventModel(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.drop_all()
db.create_all()

resource_fields = {
    "id":fields.Integer,
    "event":fields.String,
    "date":fields.String
}

add_resource_fields = {
    "id":fields.Integer,
    "event":fields.String,
    "date":fields.String
}

parser.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)
parser.add_argument(
    'date',
    type=inputs.date,
    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
    required=True
)


class EventByDate(Resource):
    @marshal_with(resource_fields)
    def get(self, start_time, end_time):
        print(start_time, end_time)
        if start_time and end_time:
            event = EventModel.query.filter(EventModel.date.between(start_time, end_time))
            if event is None:
                return EventModel.query.all()
            return event


class EventByID(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        event = EventModel.query.filter(EventModel.id == id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        return event

    def put(self, id):
        args = parser.parse_args()
        event = EventModel.query.filter(EventModel.id == id).first()

        if event is None:
            abort(404, "The event doesn't exist!")
        event.event = f"{args['event']}"
        event.date = args['date'].date()
        db.session.commit()
        return {
            "message": "The event has been updated"
        }

    def delete(self, id):
        event = EventModel.query.filter(EventModel.id == id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        db.session.delete(event)
        db.session.commit()
        return {
            "message": "The event has been deleted!"
        }


class EventsList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return EventModel.query.filter(EventModel.date == date.today()).all()


class Events(Resource):
    def post(self):
        args = parser.parse_args()
        event = f"{args['event']}"
        date = args['date'].date()

        new_event = EventModel(event=event, date=date)
        db.session.add(new_event)
        db.session.commit()

        return {
            "message": "The event has been added!",
            "event": f"{args['event']}",
            "date": f"{args['date'].date()}"
        }

    @marshal_with(resource_fields)
    def get(self):
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        if start_time and end_time:
            events = EventModel.query.filter(EventModel.date >= start_time).\
                filter(EventModel.date <= end_time).all()
            if len(events) < 1:
                abort(404, "The event doesn't exist!")
            return events
        return EventModel.query.all()


api.add_resource(Events, '/event')
api.add_resource(EventsList, '/event/today')
api.add_resource(EventByID, '/event/<int:id>')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv)>1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
