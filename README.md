# CRUD API for Google Collab
A minimal functioning API with Basic Create, Read, Update, Delete functions.
There is a functioning in memory DB which also writes its data to a .csv file
This will run inside of a Google Collab notebook.  It will write all of the 
data to the Google Collab temporary hard drive, and NGROK will give you a live
URL and Endpoint that you can use to interact with it Online.

Setup for the class of 2021 for demonstration purposes so that they can have a 
live web API, without the need to buy a server.

Built using Flask, Jsonify, JSON, NGROK.io and Raw Python

## includes:

- Endpoint that you can call over the web
- A Functioning Data Structure
- Backs up data to the temporary local hard drive provided in the Collab notebook

## missing:

- A real database
- Error Handling
- Security
- and a lot more
