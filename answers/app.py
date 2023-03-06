"""
A flask web API for the project.

It should contain the following endpoints.
/api/weather
/api/weather/stats

Both endpoints should return a JSON response
with a representation of the calculate data in my database.

The data should be stored in mysql database.
"""

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import collections
collections.MutableMapping = collections.abc.MutableMapping

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask import Flask, jsonify, render_template
from flask import request
from flask_paginate import Pagination

# Adding an OpenAPI enpoint

from flask_restplus import Namespace, Api, fields


import json
import pymysql


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="weather_stats",
)


app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

namespace = Namespace('Weather', "Weather Statistics and Data endpoints")

weather_model = namespace.model('Weather', {
    'message': fields.String(
        readonly=True,
        description='The weather message',
    )
})

api_extension = Api(
    app,
    version='1.0',
    title='Weather API',
    description='A simple weather API',
    doc='/api/docs',
    default='Weather',
    default_label=namespace.name,
    prefix='/api',
)

states: list[str] = ['nebraska', 'indiana', 'iowa', 'ohio', 'illinois']

NEW_STATE: str = states[0]


def read_jsonified_data(json_data) -> dict:
    """Read the jsonified data and return a dictionary."""
    data = json.loads(json_data)
    return data


@app.route("/api/weather", methods=["GET", "POST"])
def index():
    global NEW_STATE

    page = int(request.args.get("page", 1))
    year = request.args.get("year") or "1985"
    per_page = 10
    offset = (page - 1) * per_page

    if request.method == "POST":
        state = request.form.get("state")
        NEW_STATE = state or NEW_STATE

    table_name = str(NEW_STATE)+"_weather"

    with conn.cursor() as cursor:
        if year == "1985":
            query = f"SELECT * FROM {table_name} LIMIT %s"
            cursor.execute(query, (per_page,))

        else:
            query = f"""SELECT * FROM {table_name}
            WHERE YEAR(the_date)=%s LIMIT %s OFFSET %s"""
            cursor.execute(query, (year, per_page, offset))

        data = cursor.fetchall()

    dict_data = [dict(zip([key[0] for key in cursor.description],
                          row))
                 for row in data]

    pagination = Pagination(page=page, per_page=per_page, total=len(data))

    return render_template("index.html",
                           data=data,
                           jdata=jsonify(dict_data),
                           function=read_jsonified_data,
                           pagination=pagination,
                           year=year,
                           state=NEW_STATE.title(),
                           states=states)


@app.route('/api/weather/stats', methods=['GET', 'POST'])
def stats():

    global NEW_STATE

    state = NEW_STATE

    if request.method == "POST":
        state = request.form.get("state")

    NEW_STATE = str(state).lower() or NEW_STATE

    table_name = str(NEW_STATE)+"_stats_data"

    with conn.cursor() as cursor:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        data = cursor.fetchall()

    return render_template("stats.html",
                           data=data,
                           state=NEW_STATE.title(),
                           states=states
                           )


# api.add_resource(index, "/api/weather")
# api.add_resource(stats, "/api/weather/stats")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
