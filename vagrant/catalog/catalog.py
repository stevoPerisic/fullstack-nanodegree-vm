#!/usr/bin/env python
# 
# catalog.py -- implementation of a catalog system
#
# Vacation Rental properties
#

from flask import Flask
app = Flask(__name__)

# CRUD

# CREATE
@app.route('/rentals/new/', methods=['GET', 'POST'])
def newRental():
	"""
	POST - Creates one record of a rental property in the database.
	The database assigns a unique serial id number for the rental property.
	Automatically assigned properites are (This is handled in the SQL database schema.):
		date_time_added - time of creation of the record 
		added_by - unique id of the user that created the record
		num_of_views - number of views for this particular database record
	Args (coming in as properties of the request.form):
		name
		location
		price_day
		days_available
		num_rooms
		num_bathrooms
		pets_welcome
		description
		image

	GET - Renders a template presenting a form to allow the user to 
	insert rental property attributes into the database.
	"""
	return "This page is for adding a rental property."


# READ
@app.route('/')
@app.route('/rentals/')
def showRentals():
	"""Returns all the rental listings from the database."""
	return "This page is for viewing of rental properties."

@app.route("/rentals/<string:location>/")
def showRentalsIn(location):
	"""Returns all the rental properties in a given location."""
	return "This page is for viewing all the rentals in: %s" % location

# sort rentals by:
# 1) recently added
# 2) popular
# 3) pictures
# 4) price
# 5) proximity to user

# filters:
# 1) number of rooms
# 2) number of bathrooms
# 3) time available
# 4) pets welcome

@app.route('/rentals/<int:rental_id>/')
def showRental(rental_id):
	"""Returns one rental property from the database."""
	return "This page is for viewing rental property id:  %s" % rental_id

# UPDATE
@app.route('/rentals/<int:rental_id>/edit/', methods=['GET', 'POST'])
def editRental(rental_id):
	"""
	POST - Allows the user to update a record in the database
	Args (coming in as properties of the request.form):
		name
		location
		price_day
		days_available
		num_rooms
		num_bathrooms
		pets_welcome
		description
		image

	GET - Renders a template that presents a form allowing th euser to edit the database record.
	"""
	return "This page is for editing a rental property."

# DELETE
@app.route('/rentals/<int:rental_id>/delete/', methods=['GET', 'POST'])
def deleteRental(rental_id):
	"""
	POST - Allows the user to remove a record from the database

	GET - Renders a template that will make the user confirm the choice to delete a database record.
	"""
	return "This page is for deleting a rental property."
    
if __name__ == '__main__':
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)