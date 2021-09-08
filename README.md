# Aviyel [![CircleCI](https://circleci.com/gh/tosinolawore/aviyel/tree/master.svg?style=svg&circle-token=61288c79b79b2196594bcb0c9203292a09cad6eb)](https://circleci.com/gh/tosinolawore/aviyel/tree/master)

PROJECT DESCRIPTION
--------------------
Simple conference management system for Aviyel.

- Uses Postgres Database

PROJECT REQUIREMENTS (Required Libraries)
-----------------------------------------
All required libraries to run application detailed in requirements.txt in root.

SETTINGS
-------------------
Adjust the following settings (aviyel/settings.py) before running application in production.

```
SECRET_KEY = 'YOUR-SECRET-KEY' #Add your own secret key here
```

CI/CD Tool
-------------------
CircleCI 

```
Test result for each commit can be viewed here: https://github.com/tosinolawore/aviyel/commits/master
```

To set up CircleCI pipeline for running tests, the yaml file has been added in the following directory (
.circleci/config.yml).

Fork the entire project to your repository and afterwards, create a CircleCI account. The repository will
automatically appear on the list of Projects on circleci, you can then build and run tests.

Endpoints 
-------------------
```
Create Conference - /conferences/ (METHOD: POST, DATA: title, description, start date, end date)

Edit Conference - /conferences/<id>/ (METHOD: PUT, <id> - unique id for the conference to be edited. DATA: title, description, start date, end date)

Add Talk - /conferences/<conference_id>/talks/ (METHOD: POST, <conference_id> - unique id for the conference in which the talk is to be added. DATA: title, description, duration, date)

Edit Talk - /conferences/<conference_id>/talks/<talk_id>/ (METHOD: PUT, <conference_id> - unique id for the conference in which the talk is to be edited, <talk_id> - unique id for the talk to be edited. DATA: title, description, start date, end date)

Add Participant to a Talk - /talks/<talk_id>/participants/ (METHOD: POST, <talk_id> - unique id for the talk in which the participant is to be added. DATA: participant_id)

Delete Participant from a Talk - /talks/<talk_id>/participants/<participant_id> (METHOD: DELETE, <talk_id> - unique id for the talk in which the participant is to be deleted, <participant_id> - unique id for the participant to be deleted.)

Add Speaker to a Talk - /talks/<talk_id>/speakers/ (METHOD: POST, <talk_id> - unique id for the talk in which the speaker is to be added. DATA: speaker_id)

Delete Speaker from a Talk - /talks/<talk_id>/speakers/<speaker_id> (METHOD: DELETE, <talk_id> - unique id for the talk in which the speaker is to be deleted, <speaker_id> - unique id for the speaker to be deleted.)

List Conferences - /conferences/ (METHOD: GET)

List Talks in a Conference - /conferences/<id>/talks/ (METHOD: GET, <id> - unique id for the conference.)
```
