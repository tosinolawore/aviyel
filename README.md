﻿# Aviyel [![CircleCI](https://circleci.com/gh/tosinolawore/aviyel/tree/master.svg?style=svg&circle-token=61288c79b79b2196594bcb0c9203292a09cad6eb)](https://circleci.com/gh/tosinolawore/aviyel/tree/master)

PROJECT DESCRIPTION
--------------------
Simple conference management system for Aviyel.

- Uses Postgres Database
- Uses SQLAlchemy as ORM

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
