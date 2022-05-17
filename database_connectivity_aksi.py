import mysql.connector

def DataUpdateAksi(aksi,ruangan,pengirim,penerima,barang): 
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
    sql = """INSERT INTO LOGDATA (Robot_ID, Status, Lokasi, Tujuan, Nama_Pengirim, Nama_Penerima, Nama_Barang, Informasi_Tambahan, Help) VALUES (1, "{0}", "Base", "{1}", "{2}", "{3}", "{4}", "-", "No")""".format(aksi,ruangan,pengirim,penerima,barang)

    # val = (1, "{1}", "Base", "{2}", "{3}", "{4}", "{5}", "-", "No")

    # Executing the SQL command
    cursor.execute(sql) # , val

    # Commit your changes in the database
    conn.commit()