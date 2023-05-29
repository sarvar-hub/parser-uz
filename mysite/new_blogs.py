import sqlite3

try:
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()

    sqlite_insert_query = "SELECT * FROM blog_post ORDER BY created_on DESC, id DESC LIMIT 20;"
    

    # sqlite_insert_query = """INSERT OR IGNORE INTO blog_post
    #                     (title, link, slug, updated_on, content, created_on, status, author_id) 
    #                     VALUES 
    #                     (?, ?, ?, ?, ?, ?, ?, ?)"""
    
    # data_tuple = (title, link, slug, now, description, now, 1, 1)
    # data_tuple = ("Test2", "test2", now, "Lorem lorem toto", now, 1, 1)
    

    # cursor.execute(sqlite_insert_query, data_tuple)
    
    cursor.execute(sqlite_insert_query)
    # sqliteConnection.commit()



    records = cursor.fetchall()

    # print( records)
    for record in records:
        print(record[0])
        print(record[1])
        print(record[2])
        print(record[3])
        print(record[4])
        print()
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")