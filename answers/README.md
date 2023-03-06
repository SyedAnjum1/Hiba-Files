# Overview
--------
A flask web API for the project.

It should contain the following endpoints.
/api/weather
/api/weather/stats

Both endpoints return a JSON response
with a representation of the calculate data in my database.


# Weather Data Description
------------------------



# Problem 1 - Data Modeling
-------------------------
This module will calculate the average max temp, average min temp,
and accumulated precipitation for each Year in the database.

The data should be stored in mysql database.

# Problem 2 - Ingestion
---------------------

# Problem 3 - Data Analysis
-------------------------

# Problem 4 - REST API
--------------------

Include a Swagger/OpenAPI endpoint that provides automatic documentation of your API.

Extra Credit - Deployment
-------------------------

# Instructions for running the FLASK application.

## The following are steps to set up and run a Flask web application that displays weather statistics data:

1. Download the Python package and ensure that pip package installation is enabled during installation. This is necessary to allow for the installation of necessary Python packages used in the Flask app.

2. Download and install MySQL software to create a database for the weather statistics data.

3. Install necessary Python packages used in the Flask app using pip in the command prompt. ( use command `pip install -r requirements.txt`)

4. Create a database named "weather_stats" using MySQL commands.

5. Run the "anals.sql" and "api.sql" files using MySQL commands to create tables in the "weather_stats" database.

6. Use the "file_cleaner.py" file to extract necessary data from text files in the data folder and store it in CSV format in the csv data folder.

7. Use the "data_insertion.py" file to insert data from the CSV files into the tables created in the "weather_stats" database.

8. Use the "data_analysis.py" file to calculate new data and insert it into the tables in the "weather_stats" database.

9. Run the "app.py" file to start the Flask web application. Access the web application by opening "localhost:5000" in a web browser.

10. Use the sub-queries given in the app.py decorators to view specific pages in the web application. Tweak the URL to view whichever page is desired.

By following these steps, the Flask web application should be properly set up and display the desired weather statistics data.
