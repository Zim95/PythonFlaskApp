#Python Flask APP

#Instructions:-
1) Install python 2 or python 3 if python is not installed. On a linux based system, python comes pre-installed.

2) Dependencies include - csv, flask and json module. These modules have been locally copied and need not be installed.
   They are locally imported.
   However, for some reason if they do not work, then you will need to install them on your system.

   Installation steps:-
   WINDOWS:-
    Python2:-
      - pip install flask
      - pip install csv
      - pip install json
    Python3:-
      - pip3 install flask
      - pip3 install csv
      - pip3 install json

   LINUX:-
    Python2:-
      - python2 -m install flask
      - python2 -m install csv
      - python2 -m  install json
     Python3:-
      - python3 -m install flask
      - python3 -m install csv
      - python3 -m install json

   Import:-
   If the code doesnot run then you need to import libraries directly from the library.
    - from flask import Flask
    - import json
    - import csv

   For production, if you want to store it locally then, you type the installation command once again.
   This will give you a message that: Requirement has already been fulfilled in <directory name> directory.
   All python libraries are stored in that directory. Navigate and copy the libraries.

3) Running the code:-
   a) Navigate to the server directory and start the server:-
      WINDOWS:-
       Python2:-
        - python server.py
       Python3:-
        - PY -3 server.py
      LINUX:-
       Python2:-
        - python server.py
       Python3:-
        - python3 server.py


   b) Running front end:-
      - The front end code is contained within the template and static directories from where flask picks them up. All AJAX calls are made from the static js files.

   c) The csv file will be located in the model folder. Any changes to the csv file are to be made there.

#Configurations:-
- Configurations such as ip address and port number are stored in config.json.
- You may change the port number on config.json file.

#About :-
1) Frontend technologies used:- JQuery, AJAX, HTML5, CSS3, BootStrap4
2) For backend:- Python3.6 with flask was used.

#Working:-
- Python runs flask to run a server.
- Server continuously serves data from csv files into a json format as a RESTFUL web service.
- Javacript on the frontend makes periodic AJAX calls to update itself continuously.
- Any changes made to the CSV files are instantly reflected on the frontend dashboard.

#Features:-
- Fully responsive dashboard

#Resources:-
1) Responsive sidebar - https://bootstrapious.com/p/bootstrap-sidebar
2) Flask templating - https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python
3) Flask AJAX - https://codehandbook.org/python-flask-jquery-ajax-post/ , http://www.bogotobogo.com/python/Flask/Python_Flask_with_AJAX_JQuery.php
