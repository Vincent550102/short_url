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
        cursor.execute(
            'SELECT code FROM unuse_codes')
        has_created = cursor.fetchall()
        if len(has_created) == 0:
            codes = [("".join(st),)
                     for st in itertools.product(code_table, repeat=3)]
            shuffle(codes)
            for i in range(int(len(codes)/1000 + 1)):
                part_codes = codes[i*1000: (i+1)*1000]
                ret = cursor.executemany(
                    'INSERT INTO unuse_codes (code) VALUES (%s)', part_codes)

            self.conn.commit()
            print(ret)

    # return code or false
    def findcodeByUrlandAuthor(self, url, author):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT code FROM url_map WHERE author = %s AND url = %s', (author, url))
        result = cursor.fetchall()
        print('findcodeByUrlandAuthor result:', result)
        if len(result) > 0:
            return result[0][0]
        else:
            return False

    # find unused code
    def allocatelCode(self, url, ip):
        # prevent rebuild url by same author
        prev_code = self.findcodeByUrlandAuthor(url, ip)
        if prev_code:
            return prev_code
        cursor = self.conn.cursor()
        cursor.execute('SELECT MIN(id), code FROM unuse_codes')
        result = cursor.fetchall()
        cursor.execute(
            'DELETE FROM unuse_codes WHERE code = %s', (result[0][1], ))
        print('allocatelCode result:', result)
        self.conn.commit()
        self.insert(result[0][1], url, ip)
        return result[0][1]

    # return data(code, url)
    def findByAuthor(self, author):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT code,url,clicked FROM url_map WHERE author = %s', (author,))
        result = cursor.fetchall()
        print('findByAuthor result:', result)
        if len(result) > 0:
            return result
        else:
            return False

    # return data or false
    def findByCode(self, code):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM url_map WHERE code = %s', (code,))
        result = cursor.fetchall()
        print('findByCode result:', result)
        if len(result) > 0:
            return result[0][2]
        else:
            return False

    def codeClicked(self, code):
        cursor = self.conn.cursor()
        cursor.execute('SELECT clicked FROM url_map WHERE code = %s', (code,))
        result = cursor.fetchall()[0][0]
        print("clicked time:", result)
        cursor.execute(
            'UPDATE url_map SET `clicked`=%s WHERE code=%s', (str(result+1), code))
        self.conn.commit()

    # insert data(code, url, author) to db

    def insert(self, code, url, author):
        cursor = self.conn.cursor()
        ret = cursor.execute(
            'INSERT INTO url_map (code, url, author, clicked) VALUES (%s, %s, %s, 0)', (code, url, author))
        self.conn.commit()
