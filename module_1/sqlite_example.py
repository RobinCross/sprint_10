import sqlite3
import queries as q


# step 0 - Import sqlite3
import sqlite3

# step 1
# Connect to the database
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - make the cursor
cursor = connection.cursor()


# step 3 -write a query
# see queries.py file

# step 4 - Execute the query on the cursor and fetch the results
# pulling the results from the query
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
