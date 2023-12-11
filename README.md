# COMP3074 HAI CW

## Project Description
This report will detail the functionality and implementation of a restaurant booking chat bot system. The key aims of the system are to allow the user to find information about and make reservations at restaurants entirely within the chat feed, with additional generic chatbot features like small talk and question answering.

The main body of the chatbot has three features: name management, question answering and small talk, and an intent matching system that determines which of these categories the user’s input fall under, or if the user’s intent was to go straight to the restaurant or discover what the restaurant booking system could do. It also allows for shortcuts to be used straight into the restaurant system for users that are already experienced with the program. The restaurant part of the system is divided into four features: making a reservation, editing a reservation, cancelling a reservation, and getting information about the restaurants. 
The system stores the user’s username within the session, and it is used throughout. It saves restaurant reservations to file, so they can be viewed, edited, and cancelled in the same session or in another. 


## Features
- Name management
- Question answering
- Small talk
- Finding information on restaurants
- Making a reservation
- Editing a reservation
- Cancelling a reservation

## To Do
- [ ] Unit Tests
- [ ] Personalisation of smalltalk (date/time/weather)
- [ ] Sanity checks on reservation inputs (formating, dates, opening times)
- [ ] Change restaurant csv system to SQLite
- [ ] Recomendation system