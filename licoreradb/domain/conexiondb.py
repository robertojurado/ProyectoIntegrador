import mysql.connector

class Conexion:

  def __init__(self, host, port, user, passwd, database):
    self.__host = host
    self.__port = port
    self.__user = user
    self.__passwd = passwd
    self.__database = database

  def connect_database(self):
    try:
      conexion = mysql.connector.connect(host=self.__host, port=self.__port, user=self.__user, passwd=self.__passwd,
                                         database=self.__database)
      if conexion.is_connected():
        return conexion
    except Exception as ex:
      print(ex)