import sqlite3


class Mysql(object):

    def __init__(self, db_path=r'C:\Users\f1331853\Evan_lib', db_name='haha_sql'):
        self.db_name = db_name
        self.db_path = db_path + '/' + self.db_name
        # connection Mysql
        self.cxn, self.cur = self._connect()

    def _connect(self):
        self.cxn = sqlite3.connect(self.db_path)
        self.cur = self.cxn.cursor()
        return self.cxn, self.cur

    def create(self):
        try:
            self.cur.execute('''
            CREATE TABLE users(
                uid INTEGER,
                prid INTEGER)
            ''')
        except Exception as e:
            print('Create Table Error, ERROR-MSG: [ {} ]'.format(e))
            print('Recreate the users now!')
            self.cur.execute('DROP TABLE users')
            self.create()

    def db_dump(self):
        print('Mysql dump:')
        self.cur.execute('SELECT * FROM users')
        for eachline in self.cur.fetchall():
            print(eachline)


if __name__ == '__main__':
    mysql = Mysql()
    mysql.create()

    mysql.cur.execute('INSERT INTO users VALUES(100, 200)')
    mysql.db_dump()

    mysql.cur.close()
    mysql.cxn.commit()
    mysql.cxn.close()
