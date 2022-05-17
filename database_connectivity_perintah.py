import mysql.connector

def DataUpdatePerintah(perintah,parameter): 
    #Establishing the connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ta1"
    )

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing SQL query to INSERT a record into the database.
    sql = """INSERT INTO COMMAND (Perintah,Params) VALUES ("{0}", "{1}")""".format(perintah,parameter)

    # val = (1, "{1}", "Base", "{2}", "{3}", "{4}", "{5}", "-", "No")

    # Executing the SQL command
    cursor.execute(sql) # , val

    # Commit your changes in the database
    conn.commit()