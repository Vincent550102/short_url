import mysql.connector
import configparser
import itertools
from random import shuffle

class DataBase:
    def __init__(self):
        # Use database config in config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.conn = mysql.connector.connect(**config['database'])

        # Clear and initialize database
        with open('schema.sql') as file:
            cmds = file.read().split(';')
            cursor = self.conn.cursor()
            for cmd in cmds:
                cursor.execute(cmd)
            self.conn.commit()

        cursor = self.conn.cursor()
        code_table = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
        codes = [("".join(st),) for st in itertools.product(code_table, repeat=3)]
        shuffle(codes)
        for i in range(int(len(codes)/1000 +1)):
            part_codes = codes[i*1000: (i+1)*1000]
            ret = cursor.executemany('INSERT INTO unuse_codes (code) VALUES (%s)', part_codes)

        self.conn.commit()
        print(ret)

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
    def allocatelCode(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT MIN(id), code FROM unuse_codes')
        result = cursor.fetchall()
        cursor.execute('DELETE FROM unuse_codes WHERE code = %s', (result[0][1], ))
        print('findUnusedCode result:',result)
        self.conn.commit()
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
        ret = cursor.execute('INSERT INTO url_map (code, url, author) VALUES (%s, %s, %s)', (code, url, author))
        self.conn.commit()

