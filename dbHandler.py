import pymysql

def insertData(data):
    rowId = 0

    try:
        # Establish the connection to the database
        db = pymysql.connect(
            host="localhost",
            user="criminaluser",
            password="your_password",  # Replace with the actual password
            database="criminaldb"
        )
        cursor = db.cursor()
        print("Database connected")

        # Ensure the data is passed correctly with parameterized query to prevent SQL injection
        query = """
            INSERT INTO criminaldata 
            (Name, `Father's Name`, `Mother's Name`, Gender, 
            `Blood Group`, `Identification Mark`, Nationality, Religion, `Crimes Done`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        # Prepare the data as a tuple
        data_tuple = (
            data["Name"],
            data["Father's Name"],
            data["Mother's Name"],
            data["Gender"],
            #data["DOB"],
            data["Blood Group"],
            data["Identification Mark"],
            data["Nationality"],
            data["Religion"],
            data["Crimes Done"]
        )

        # Execute the query
        cursor.execute(query, data_tuple)

        # Commit the changes to the database
        db.commit()
        
        # Get the ID of the inserted row
        rowId = cursor.lastrowid
        print(f"Data stored on row {rowId}")

    except Exception as e:
        # If an error occurs, rollback the transaction
        db.rollback()
        print(f"Data insertion failed: {e}")
    
    finally:
        # Close the database connection
        db.close()
        print("Connection closed")
    
    return rowId

def retrieveData(name):
    id = None
    crim_data = None

    try:
        # Establish the connection to the database
        db = pymysql.connect(
            host="localhost",
            user="criminaluser",
            password="your_password",  # Replace with the actual password
            database="criminaldb"
        )
        cursor = db.cursor()
        print("Database connected")

        # Perform a parameterized query to avoid SQL injection
        query = "SELECT * FROM criminaldata WHERE name=%s"
        
        # Execute the query
        cursor.execute(query, (name,))
        
        # Fetch the result
        result = cursor.fetchone()

        if result:
            id = result[0]
            crim_data = {
                "Name": result[1],
                "Father's Name": result[2],
                "Mother's Name": result[3],
                "Gender": result[4],
                #"DOB(yyyy-mm-dd)": result[5],
                "Blood Group": result[6],
                "Identification Mark": result[7],
                "Nationality": result[8],
                "Religion": result[9],
                "Crimes Done": result[10]
            }
            print("Data retrieved")
        else:
            print(f"No data found for name: {name}")

    except Exception as e:
        print(f"Error: Unable to fetch data. {e}")

    finally:
        # Close the database connection
        db.close()
        print("Connection closed")

    return id, crim_data
