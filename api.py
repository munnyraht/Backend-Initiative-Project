from flask import Flask, request

import json

# import requests

app = Flask(__name__)

with open('users.json') as f:
    users = json.load(f)

with open('movies.json') as f:
    movies = json.load(f)

with open('rentals.json') as f:
    rentals = json.load(f)


#  Get all users
@app.route('/api/user', methods=['GET'])
def get_users():
    return {"message": "Users Retrieved Successfully",
            "userData": users
            }


# Create user
@app.route('/api/user', methods=['POST'])
def create_user():
    request_json = request.json
    username = request_json.get('username')
    email = request_json.get('email')
    password = request_json.get('password')
    latest_id = users[-1]['id']
    user_data = {"id": latest_id + 1, 'username': username, 'email': email, 'password': password}
    users.append(user_data)
    with open("users.json", "w") as jsonFile:
        json.dump(users, jsonFile)
    return {"message": "User created successfully",
            "userData": users}


# Get user by ID
@app.route('/api/user/<id>', methods=['GET'])
def get_user_by_id(id):
    for i in range(len(users)):
        if users[i]['id'] == int(id):
            user = users[i]
            return {
                "message": "User {} retrieved successfully".format(id),
                "userData": {
                    "id": user['id'],
                    "username": user['username'],
                    "email": user['email'],
                    "password": user['password']
                }
            }
    return {}


# Update user
@app.route('/api/user/<id>', methods=['PATCH'])
def update_user(id):
    for i in range(len(users)):
        if users[i]['id'] == int(id):
            user = users[i]
            request_json = request.json
            # if data is not provided, it takes the previous user data
            username = request_json.get('username', user['username'])
            email = request_json.get('email', user['email'])
            password = request_json.get('password', user['password'])
            users[i]['username'] = username
            users[i]['email'] = email
            users[i]['password'] = password
            with open("users.json", "w") as jsonFile:
                json.dump(users, jsonFile)
            return {
                "message": "User updated successfully",
                "userData": users[i]}
    return {}


# Delete user
@app.route('/api/user/<id>', methods=['DELETE'])
def delete_user(id):
    for i in range(len(users)):
        if users[i]['id'] == int(id):
            del users[i]
            break
    with open("users.json", "w") as jsonFile:
        json.dump(users, jsonFile)
    return {
        "message": f"User with ID {id} deleted successfully",
        "userData": users}


# create movie
@app.route('/api/movie', methods=['POST'])
def create_movie():
    request_json = request.json
    name = request_json.get('name')
    genre = request_json.get('genre')
    description = request_json.get('description')
    latest_id = movies[-1]['id']
    new_movie = {"id": latest_id + 1, "name": name, "desciption": description, "genre": genre}
    movies.append(new_movie)
    with open("movies.json", "w") as jsonFile:
        json.dump(movies, jsonFile)
    return {
        "message": "Movie created successfully",
        "movieData": movies}


# Update Movie
@app.route('/api/movie/<id>', methods=['PATCH'])
def update_movies(id):
    for i in range(len(movies)):
        if movies[i]['id'] == int(id):
            movie = movies[i]
            request_json = request.json
            # if data is not provided, it takes the previous movie data
            name = request_json.get('name', movie['name'])
            description = request_json.get('description', movie['description'])
            genre = request_json.get('genre', movie['genre'])
            movies[i]['name'] = name
            movies[i]['description'] = description
            movies[i]['genre'] = genre
    with open("movies.json", "w") as jsonFile:
        json.dump(movies, jsonFile)
    return {
        "message": "Movie updated successfully",
        "movieData": movies
    }


# Get all movies
@app.route('/api/movie', methods=['GET'])
def get_movies():
    return {
        "message": "Movies retrieved successfully",
        "movieData": movies
    }


# Get movie by ID
@app.route('/api/movie/<id>', methods=['GET'])
def get_movie_by_id(id):
    for i in range(len(movies)):
        if movies[i]['id'] == int(id):
            movie = movies[i]
            return {
                "message": "User {} retrieved successfully".format(id),
                "userData": {
                    "id": movie['id'],
                    "username": movie['name'],
                    "email": movie['description'],
                    "password": movie['genre']
                }
            }
    return {}


# Delete movie
@app.route('/api/movie/<id>', methods=['DELETE'])
def delete_movie(id):
    for i in range(len(movies)):
        if movies[i]['id'] == int(id):
            del movies[i]
            break
    with open("movies.json", "w") as jsonFile:
        json.dump(movies, jsonFile)
    return {
        "message": "Movie deleted successfully",
        "movieData": movies
    }


# Create Rentals
@app.route('/api/rental', methods=['POST'])
def create_rentals():
    request_json = request.json
    item = request_json.get('item')
    borrowing_days = request_json.get('borrowing_days')
    vendor = request_json.get('vendor')
    latest_id = rentals[-1]['id']
    new_rental = {"id": latest_id + 1, "item": item, "borrowing_days": borrowing_days, "vendor": vendor}
    rentals.append(new_rental)
    with open("rentals.json", "w") as jsonFile:
        json.dump(rentals, jsonFile)
    return {
        "message": "Rental created successfully",
        "rentalData": rentals
    }


# Get all rentals
@app.route('/api/rental', methods=['GET'])
def get_rentals():
    return {
        "message": "Rentals retrieved successfully",
        "rentalData": rentals
    }


# Get rental by ID
@app.route('/api/rental/<id>', methods=['GET'])
def get_rental_by_id(id):
    for i in range(len(rentals)):
        if rentals[i]['id'] == int(id):
            rental = rentals[i]
            return {
                "message": "User {} retrieved successfully".format(id),
                "userData": {
                    "id": rental['id'],
                    "username": rental['item'],
                    "email": rental['borrowing_days'],
                    "password": rental['vendor']
                }
            }
    return {}


# Update Operation
@app.route('/api/rental/<id>', methods=['PATCH'])
def update_rentals(id):
    request_json = request.json
    item = request_json.get('item')
    borrowing_days = request_json.get('borrowing_days')
    vendor = request_json.get('vendor')
    for i in range(len(rentals)):
        if rentals[i]['id'] == int(id):
            rentals[i]['item'] = item
            rentals[i]['borrowing_days'] = borrowing_days
            rentals[i]['vendor'] = vendor
    with open("rentals.json", "w") as jsonFile:
        json.dump(rentals, jsonFile)
    return {
        "message": "Rental updated successfully",
        "rentalData": rentals
    }


# Delete Operation
@app.route('/api/rental/<id>', methods=['DELETE'])
def delete_rentals(id):
    for i in range(len(rentals)):
        if rentals[i]['id'] == int(id):
            del rentals[i]
            break
    with open("rentals.json", "w") as jsonFile:
        json.dump(rentals, jsonFile)
    return {
        "message": "Rental with ID {} deleted successfully".format(id),
        "rentalData": rentals
    }
