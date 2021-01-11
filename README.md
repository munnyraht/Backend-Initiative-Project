# Backend-Initiative-Project
This is a base repository for the backend initiative project

## Level One Task: CRUD API WITH ARRAY
Build a CRUD(Create, Read, Update, Delete) API(Application Programming Interface) with any  backend language of your choice.
No database involved, just a server.

The endpoints will be for Users, Movies, Rentals.

Submission: Publish the APIs with Postman and share this too, do not forget to include the link to your level one task branch.

Reviews will be done on Saturdays.

To run this file run 'python wsgi.py in terminal'.


files :

* api.py - contains 4 endpoints
    * create_user : takes username and a list of genre and creates a user with these information
    * get_users : uses a GET requests that fetches all registered users.
    * update_rentals : updates the rental dictionary, its takes 'movie' and 'rental_count' from a POST request.
    * delete_movie : deletes movie from the current movie list. It takes 'movie' which a an existing movie name from a POST request
* wsgi.py - contains code that run starts a local server for api.py
* requirements.txt
