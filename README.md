# gt-takehome-first-draft

# Overview
This project is a Flask API that consumes data from endpoints in the [Wikipedia API](https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews) and can be used to retrieve:
- A ranked list of the most viewed articles for a week
- A ranked list of the most viewed articles for a month
- The total view count for an article for a week
- The total view count for an article for a month
- The day of the month an article had the most views

---

# How to run this app
## Step 0: Install venv
If you do not already have venv installed, you can install it using the commands below:

For Unix/macOS: `python3 -m pip install --user virtualenv`<br>
For Windows: `py -m pip install --user virtualenv`<br>

## Step 1: Virtual Environment Setup and Activation
Select a file directory location to create the virtual environment (the same location you cloned this repo to is fine).

> Note: In the following commands, the name of the virtual environment created is "env". If you wish, you can choose another string to name the virtual environment.

In your selected location, run:<br>
For Unix/macOS: `python3 -m venv env`<br>
For Windows: `py -m venv env`<br>

To activate your virtual environment, run:<br>
For Unix/macOS: `source env/bin/activate`<br>
For Windows: `.\env\Scripts\activate`<br>

You can confirm you’re in the virtual environment by checking the location of your Python interpreter:<br>
For Unix/macOS: `which python` should result in: `.../env/bin/python`<br>
For Windows: `where python` should result in: `...\env\Scripts\python.exe`<br>

When you're done, you can leave the virtual environment by running `deactivate`

## Step 2: Installing dependencies and running local app
In a CLI inside the cloned repo location, run:<br>
For Unix/macOS: `python3 -m pip install -r requirements.txt`<br>
For Windows: `py -m pip install -r requirements.txt`<br>

To run the app, run:<br>
For Unix/macOS: `python app.py`<br>
For Windows: `py app.py`<br>

---

# Using the API
Once up and running, you can find full documentation of the API endpoints at http://localhost:8000/api/ui/

You can either use curl in a separate console window to make calls to the endpoints, or you can use the Swagger API