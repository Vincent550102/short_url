import mysql.connector

db_settings = {
    'host': 'localhost',
    'user': 'root',
    'password': '5jz83j6ji3',
    'database': 'shorten_url',
    'charset': 'utf8',
    'auth_plugin': 'mysql_native_password',
}

class DataBase:
    def __init__(self):
        db = mysql.connector.connect(**db_settings)

        # Clear and initialize database
        with open('schema.sql') as file:
            codes = file.read()
            cursor = db.cursor()
            cursor.execute(codes, multi=True)

    # return code or false
    def findcodeByUrl(self, url):
        pass

    # find unused code
    def findUnusedCode():
        pass

    # return data(code, url)
    def findByAuthor():
        pass

    # return data or false
    def findByCode():
        pass

    # insert data(code, url, author) to db
    def insert():
        pass