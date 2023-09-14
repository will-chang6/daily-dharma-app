#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response 
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User, CalendarEntry, JournalEntry, JournalPrompt

# Add your model imports


# Views go here!
@app.route('/')
def index():
    return '<h1>Phase 5 Project Server</h1>'

class Users(Resource): 
    def get(self): 
        if session.get('user_id'):
             user = User.query.filter(User.id == session['user_id']).first()
             return make_response(user.to_dict(), 200)

        return {'error': '401 Unauthorized'}, 401

class Logout(Resource):
    def delete(self): 
        session['user_id'] = None

        return make_response({}, 204)

class JournalPrompts(Resource):
    def get(self): 
        prompts = [prompt.to_dict(rules=('-journal_entries',)) for prompt in JournalPrompt.query.all()]
        return make_response(prompts, 200)

api.add_resource(JournalPrompts, '/prompts')
api.add_resource(Users, '/users')
api.add_resource(Logout, '/logout')



if __name__ == '__main__':
    app.run(port=5555, debug=True)
