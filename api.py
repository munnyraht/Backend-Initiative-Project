from flask import Flask
import json

app = Flask(__name__)


@app.route('/users',methods = ['POST', 'GET'])

def user():
	users = ['Tobi', 'Shola', 'Bola']
	# print(users[0])
	return {'users':users}





@app.route('/movies',methods = ['POST', 'GET'])

def movies():
	movies = ["Queen's Gambit", 'TENET', 'Old Guard' , 'Designator Survivor']
	# print(users[0])
	return {'Movies':movies}


@app.route('/rentals',methods = ['POST', 'GET'])

def rentals():
	rentals = {"Queen's Gambit": 50, 'TENET': 20, 'Old Guard': 40 , 'Designator Survivor': 60}
	# print(users[0])
	return rentals



