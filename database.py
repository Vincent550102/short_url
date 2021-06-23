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
        self.conn = mysql.connector.connect(**db_settings)

        # Clear and initialize database
        with open('schema.sql') as file:
            cmds = file.read().split(';')
            cursor = self.conn.cursor()
            for cmd in cmds:
                cursor.execute(cmd)
            self.conn.commit()

    # return code or false
    def findcodeByUrl(self, url):
        cursor = self.conn.cursor()
        cursor.execute('SELECT code FROM url_map WHERE url = %s', (url,))
        result = cursor.fetchall()
        print('findcodeByUrl result:',result)
        if len(result) > 0:
            return result[0][0]
        else:
            return False


    # find unused code
    def findUnusedCode(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT MIN(id), code FROM unuse_codes')
        result = cursor.fetchall()
        print('findUnusedCode result:',result)
        return result[0][1]

    # return data(code, url)
    def findByAuthor(self, author):
        cursor = self.conn.cursor()
        cursor.execute('SELECT code,url FROM url_map WHERE author = %s', (author,))
        result = cursor.fetchall()
        print('findByAuthor result:',result)
        if len(result) > 0:
            return result[0]
        else:
            return False

    # return data or false
    def findByCode(self, code):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM url_map WHERE code = %s', (code,))
        result = cursor.fetchall()
        print('findByCode result:',result)
        if len(result) > 0:
            return result[0]
        else:
            return False

    # insert data(code, url, author) to db
    def insert(self, code, url, author):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO url_map (code, url, author) VALUES (%s, %s, %s)', (code, url, author))
