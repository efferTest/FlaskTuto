#!/bin/bash

export FLASK_APP=flaskr
export FLASK_ENV=development
source /home/sojen/sojenVenv/bin/activate
flask init-db
flask run
