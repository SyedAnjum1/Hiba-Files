"""Module to insert the txt data into a mysql database"""

import datetime
import logging
import mysql.connector
import os
import time


logging.basicConfig(filename="data_insertion.log", level=logging.INFO)


def log_data_insertion(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_records = result
        logging.info("Data insertion started at %s", start_time)
        logging.info("Data insertion completed at %s", end_time)
        logging.info("Total records inserted: %s", total_records)
        return result

    return wrapper


# Create a function to format dates.
def format_date(date):
    """Formats the date"""

    date = datetime.datetime.strptime(date, "%Y%m%d")
    date = date.strftime("%Y-%m-%d")

    return date


# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    password="root",
    user="root",
    database="weather_stats",
)

# Create a cursor
mycursor = mydb.cursor()


# Create a function to insert data into the table
@log_data_insertion
def insert_data(data_file):

    table = data_file.split(".")[0] + "_weather"

    records: int = 0
    with open(data_file, "r") as file:
        # Read the file
        for line in file:

            records += 1
            line = [entry.rstrip() for entry in line.split(',') if entry != '']

            # Insert the data into the database
            mycursor.execute(
                f"""INSERT INTO {table}
                (the_date, max_temp, min_temp, precipitation)
                VALUES (%s, %s, %s, %s)""",
                line,
            )

    return records


def main():
    """Main function to insert data to different tables"""

    files = [file for file in os.listdir() if file.endswith(".csv")]

    for file in files:
        insert_data(file)

    mydb.commit()

    mycursor.close()
    mydb.close()


if __name__ == "__main__":
    main()
