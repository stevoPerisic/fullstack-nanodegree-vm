## Project 3 - Item Catalog

## Project Overview
You will develop a application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

You will deliver a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. The application will properly use the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.

##Requirements
1. API Endpoints
  * Page does implement an JSON endpoint with all the required content
  * Additional API endpointssuch as RSS, Atom, or XML
2. CRUD: Read
  * Page reads category and item information from a database
  * Add an item image field that is read from the database and displayed on the page
3. CRUD: Create
  * Include a for allowing the users to add new items and correctly process submitted forms
  * Update the new item form to correctly process the inclusion of item images
4. CRUD: Update
  * Include a function to edit/update a current record in teh database table and corrcetly processed submitted forms
  * Update the dit/update form to correctly process the inclusion of item images
5. CRUD: Delete
  * Page includes a function to delete a current record
  * research and implement this function using POST requests and nonces to prevent cross-site request forgeries (CSFR)
6. Authentication and Authorization
  * Page implements a third-party authentication & authorization service; and create, delete and update operations do consider auth status prior to execution


