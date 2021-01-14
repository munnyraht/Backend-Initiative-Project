# Backend-Initiative-Project
This is a base repository for the backend initiative project


## Level Two Task: DATABASE INTEGRATIONS AND INPUT VALIDATION
Congratulations on passing the L1 task😎😎

### WELCOME TO LEVEL TWO

Your task, should you choose to accept it, is to integrate data storage using any DB of your choice eg MongoDB, MySQL, postGRES, etc. This is your chance to learn about the DB and how it works. In addition to that, you are to validate the data using any validation tool of your choice, eg Joi for NodeJS, (we don't want anyone storing wrongly formatted data to our db, do we?

Submission: Publish the APIs with Postman and share this link too, do not forget to include the link to your level two task branch.

Reviews and promotions will be done every 2 weeks.

## Level Two Task: DATABASE INTEGRATIONS AND INPUT VALIDATION
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

