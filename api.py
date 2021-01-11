from flask import Flask, request
import json
import requests

app = Flask(__name__)

users = [{'username': 'Tobi', 'genres': ['drama', 'thriller']}, {'username': 'Shola', 'genres': ['action', 'thriller']},
         {'username': 'Bola', 'genres': ['drama', 'action']}]

movies = ["Queen's Gambit", 'TENET', 'Old Guard', 'Designator Survivor']

rentals = {"Queen's Gambit": 50, 'TENET': 20, 'Old Guard': 40, 'Designator Survivor': 60}


# Create operation
@app.route('/create_user', methods=['POST'])
def create_user():
    request_json = request.json
    username = request_json.get('username')
    genres = request_json.get('genres')
    user_data = {'username': username, 'genres': genres}
    print(user_data)
    users.append(user_data)
    return 'User Created Successfully'


# Read operation
@app.route('/get_users', methods=['POST', 'GET'])
def get_users():
    return json.dumps({'users': users})


# Update Operation
@app.route('/update_rentals', methods=['POST'])
def update_rentals():
    request_json = request.json
    movie = request_json.get('movie')
    rental_count = request_json.get('rental_count')
    rentals[movie] = rental_count
    print(rentals)
    return 'Rentals Created Successfully'


# Delete Operation
@app.route('/delete_movie', methods=['POST'])
def delete_movie():
    request_json = request.json
    movie = request_json.get('movie')
    try:
        movies.remove(movie)
    except ValueError:
        return 'Could not delete movie'
    print(movies)
    return 'Movie Deleted Successfully'
