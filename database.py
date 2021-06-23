import pymysql

db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "db": "short_url",
    "charset": "utf8"
}

class DataBase:
    def __init__(self):
        conn = pymysql.connect(**db_settings)

        # Clear and initialize database
        with conn.cursor() as cursor:
            with open('schema.sql') as file:
                codes = file.read()
                print(codes)
                cursor.execute(codes)

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