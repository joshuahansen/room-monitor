import MySQLdb


class Database():
    """
    def __init__(self, user, passwd, host='localhost'):
        self.host = host
        self.user = user
        self.passwd = passwd

        self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd)
    """
    def insert_humidity(self, humidity):
        sql = "INSERT INTO humidity(time, humidity) VALUES(NOW(), {});".format(humidity)
        print(sql)


db = Database()
db.insert_humidity(123)
