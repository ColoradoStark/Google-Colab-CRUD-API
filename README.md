# CRUD API for Google Collab
A minimal functioning API with Basic Create, Read, Update, Delete routes.
There is a functioning in memory DB which also writes its data to a .csv file
It will run inside of a Google Collab notebook.  You will get a live
URL Endpoint that you can use to make HTTP requests, and a .csv file will 
be written to the notebook's virtual hard drive so that you can verify 
everything is working as expected.

Setup for the class of 2021 so that they can code and make requests to a live web 
API, without the need to buy a server.  For testing purposes only, this should not
be used in production.

Built using Flask, Jsonify, JSON, NGROK.io and Raw Python

## includes:

- Endpoint that you can call over the web
- A Functioning Data Structure
- Backs up data to the temporary local hard drive provided in the Collab notebook

## missing:

- Error Handling
- Security
- Logging
- Authentication
- Query
- and a lot more
