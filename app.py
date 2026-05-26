from flask import Flask, render_template
from datetime import date, timedelta
from requests import get
import csv
import pandas as pd
import json
# import psycopg2

app = Flask(__name__, static_url_path='', static_folder='./frontend/static',
            template_folder='./frontend/templates')


@app.route("/")
def frontpage():
    # Show front page
    return render_template("index.html")


@app.route("/spottedlanternfly")
def slfly():
    # Open observations CSV (from iNaturalist export tool)
    df = pd.read_csv('./frontend/static/js/lanternfly/observations.csv')
    observation_dict = df.to_dict(orient='records')
    # Convert to geoJSON
    geoJSON = {"type": "FeatureCollection", "features": []}
    for observation in observation_dict:
        geoJSON["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [observation['longitude'], observation['latitude']]
            },
            "properties": {
                "observationTime": observation['created_at'],
                "url": observation['url'],
                "place": observation['place_guess'],
                "id": observation['id']
            }
        })

    # Show lanternfly page
    return render_template("lanternfly.html", lanternflyData=geoJSON)


@app.route("/current")
def currentProjects():
    # Show current projects page
    return render_template("current.html")


@app.route("/occurrence-records")
def occurrenceRecords():
    # Show occurrence records page
    return render_template("occurrence_records.html")


@app.route("/me")
def aboutme():
    # Show about me page
    return render_template("me.html")


@app.route("/contact")
def contact():
    # Show contact page
    return render_template("contact.html")


@app.route("/discography", methods=['GET', 'POST'])
def discography():
    # Open select_discography.csv and read into variable
    with open('./frontend/static/select_discography.csv', newline='') as f:
        discography_data = list(csv.reader(f))
        disc_count = len(discography_data)

    # Show discography page
    return render_template("discography.html", discographyData=discography_data, discCount=disc_count)


@app.route("/projects")
def projects():
    # Show projects page
    return render_template("projects.html")


@app.route("/touchgrass")
def touchgrass():
    # Show touch grass page
    return render_template("touchgrass.html")

# @app.route("/sound-explorer")
# def sound_explorer():
#     # Show sound explorer page
#     return render_template("sound-explorer.html")

# @app.route("/entomology-entries")
# def entomology_entries():
#     # Get CSV for

# Presentation for weatherblanket versions
# @app.route("/presentation")
# def presentation():
#     # Show touch grass page
#     return render_template("presentation.html")
