"""
This module will calculate the average max temp, average min temp,
and accumulated precipitation for each Year in the database.
"""

# Import the necessary modules
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    password="root",
    user="root",
    database="weather_stats",
)


# Create a cursor
mycursor = mydb.cursor()


# Create a function that will store the stats data into
# tables in the database.
def store_yearly_stats(place, data):
    """Storing stats in the place_tables"""

    place_data_table = place.removesuffix("_weather") + "_stats_data"

    query = f"""INSERT INTO {place_data_table}
    (year, average_max_temp, average_min_temp, precipitation_sum)
    VALUES (%s, %s, %s, %s)"""

    mycursor.execute(query, data)
    mydb.commit()


# Create a function to calculate the average max temp, average min temp,
# and accumulated precipitation for each Year in the database.
def calculate_yearly_stats():
    """Average min temp and Average max temp"""

    query = "SHOW TABLES"
    mycursor.execute(query)
    results = mycursor.fetchall()

    spec_years, spec_tables, data, new_data = [], [], [], []

    # Create a list of tables
    if results:
        spec_tables = [table[0] for table in results
                       if table[0].endswith("_weather")]

    # Create a list of the average max temp, average min temp,
    # and accumulated precipitation for each Year in the database.
    for table in spec_tables:
        year_query = f"SELECT DISTINCT YEAR(the_date) FROM {table}"
        mycursor.execute(year_query)
        years = mycursor.fetchall()

        # Create a list of years
        if years:
            spec_years = [year[0] for year in years]

        for year in spec_years:
            mycursor.execute(f"""SELECT AVG(max_temp), AVG(min_temp),
            SUM(precipitation)FROM {table} WHERE YEAR(the_date) = {year}""")
            data = mycursor.fetchall()
            if data:
                new_data = [year] + [float(datum) for datum in data[0]]

            # print(new_data)
            store_yearly_stats(table, new_data)

            # Print the results
            print(f"{table} for {year}: {data}")

    return data


def main():
    """Main function to calculate the average max temp, average min temp,
    and accumulated precipitation for each Year in the database."""

    calculate_yearly_stats()

    mycursor.close()
    mydb.close()


if __name__ == "__main__":
    main()
