import mysql.connector
from mysql.connector.errors import Error

from domain.conexiondb import Conexion

# Crear la clase producto

class producto:

  def __init__(self, id_producto, nombre_producto, precio_producto, contenido_mililitros, stock):
    self._id_producto = id_producto
    self._nombre_producto = nombre_producto
    self._precio_producto = precio_producto
    self._contenido_mililitros = contenido_mililitros
    self._stock = stock

  @property
  def id_producto(self):
    return self._id_producto

  @id_producto.setter
  def id_producto(self, idProducto):
    self._id_producto = idProducto

  @property
  def nombre_producto(self):
    return self._nombre_producto

  @nombre_producto.setter
  def nombre_producto(self, nombreProducto):
    self._nombre_producto = nombreProducto

  @property
  def precio_producto(self):
    return self._precio_producto

  @precio_producto.setter
  def precio_producto(self, precioProducto):
    self._precio_producto = precioProducto

  @property
  def contenido_mililitros(self):
    return self._contenido_mililitros

  @contenido_mililitros.setter
  def contenido_mililitros(self, contenidoMililitros):
    self._contenido_mililitros = contenidoMililitros

  @property
  def stock(self):
    return self._stock

  @stock.setter
  def stock(self, stock):
    self._stock = stock


  @staticmethod
  def crear_producto():

    print("************ Crear Producto ************ \n")

    _nombre_producto = input("Por favor escribe el nombre del producto. \n")

    _precio_producto = input("Por favor escribe el precio del producto \n")
    while _precio_producto.isnumeric() == False or int(_precio_producto) < 0:
      _precio_producto = input("Por favor escribe el precio del producto \n")
    _precio_producto = int(_precio_producto)

    _contenido_mililitros = input("Por favor escribe el contenido en mililitros del producto \n")
    while not (_contenido_mililitros.isnumeric()) and int(_contenido_mililitros) < 0:
      _contenido_mililitros = input("Por favor escribe el contenido en mililitros del producto \n")
    _contenido_mililitros = int(_contenido_mililitros)

    _stock = input("Por favor escribe el stock del producto \n")
    while not (_stock.isnumeric()) and int(_stock) < 0:
      _stock = input("Por favor escribe el stock del producto \n")
    _stock = int(_stock)


    conexion = Conexion(host="localhost", port=3306, user="root", passwd="", database="licorera")
    conn = conexion.connect_database()
    cursor = conn.cursor()
    datos = (_nombre_producto, _precio_producto, _contenido_mililitros, _stock)
    try:
      sql = "INSERT INTO producto(nombre_producto, precio_producto, contenido_mililitros, stock) VALUES(%s,%s,%s,%s)"
      cursor.execute(sql,datos)
      conn.commit()
      conn.close()
      print("Producto creado exitosamente. \n")
    except Error as err:
      print("Ha ocurrido el error "+str(err))
      conn.close()

  @staticmethod
  def buscar_producto():
    print("************ Buscar Producto ************")
    conexion = Conexion(host="localhost", port=3306, user="root", passwd="", database="licorera")
    conn = conexion.connect_database()
    cursor = conn.cursor()

    _nombre_producto = input("Por favor escribe el nombre del producto que deseas consultar. \n")

    try:
     sql = ("SELECT `id_producto`, `nombre_producto`, `precio_producto`, contenido_mililitros, stock FROM `producto` "
            "WHERE nombre_producto = '")+_nombre_producto+"'"
     cursor.execute(sql)
     print(f"{"Código":>25}{"Nombre producto":>25}{"Precio":>25}{"Contenido (ml)":>25}{"Stock":>25}")
     fila = cursor.fetchone()
     print(f"{fila[0]:>25}{fila[1]:>25}{fila[2]:>25}{fila[3]:>25}{fila[4]:>25}")
     conn.close()
    except Error as err:
      print("Ha ocurrido el error: "+str(err))
      conn.close()

  @staticmethod
  def editar_producto():
    print("********** Editar Producto ************\n")

    conexion = Conexion(host="localhost", port=3306, user="root", passwd="", database="licorera")
    conn = conexion.connect_database()
    cursor = conn.cursor()

    _nombre_producto = input("Por favor escribe el nombre del producto que deseas actualizar. \n")

    try:
      sql = ("SELECT `id_producto`, `nombre_producto`, `precio_producto`, contenido_mililitros, stock FROM `producto` "
             "WHERE nombre_producto = '") + _nombre_producto + "'"
      cursor.execute(sql)
      print(f"{"Código":>25}{"Nombre producto":>25}{"Precio":>25}{"Contenido (ml)":>25}{"Stock":>25}")
      fila = cursor.fetchone()
      print(f"{fila[0]:>25}{fila[1]:>25}{fila[2]:>25}{fila[3]:>25}{fila[4]:>25}")


      editar = input("Deseas modificar algún dato del producto? En caso afirmativo, presiona s. En otro caso presiona otra"
                     "tecla")

      while editar == "s":

        opcion = input("Selecciona una de las siguientes opciones: \n"
              "1. Modificar el nombre del producto. \n"
              "2. Modificar el precio del producto. \n"
              "3. Modificar el contenido en mililitros del producto. \n"
              "4. Modificar la cantidad de unidades disponibles del producto.\n"
              "5. Salir. \n")

        while not(opcion.isnumeric()) or int(opcion) < 0 or int(opcion) > 6:
          opcion = input("Selecciona una de las siguientes opciones: \n"
                         "1. Modificar el nombre del producto. \n"
                         "2. Modificar el precio del producto. \n"
                         "3. Modificar el contenido en mililitros del producto. \n"
                         "4. Modificar la cantidad de unidades disponibles del producto.\n"
                         "5. Salir. \n")

        opcion = int(opcion)

        if opcion == 1:
          nombre = input("Escribe el nuevo nombre del producto. \n")
          cursor2 = conn.cursor()
          sql = "UPDATE producto SET nombre_producto = '"+nombre+"' WHERE nombre_producto = '"+_nombre_producto+"'"
          cursor2.execute(sql)
          conn.commit()
          conn.close()
          print("El producto fue modificado exitosamente. \n")

        elif opcion == 2:
          precio = input("Escribe el nuevo precio del producto. \n")
          while not(precio.isnumeric()) or int(precio) < 0:
            precio = input("Escribe el nuevo precio del producto. \n")
          precio = int(precio)

          cursor2 = conn.cursor()
          sql = "UPDATE producto SET precio_producto = "+str(precio)+" WHERE nombre_producto = '"+_nombre_producto+"'"
          cursor2.execute(sql)
          conn.commit()
          conn.close()
          print("El producto fue modificado exitosamente. \n")

        elif opcion == 3:
          contenido = input("Escribe el nuevo contenido en mililitros del producto. \n")
          while not(contenido.isnumeric()) or int(contenido) < 0:
            contenido = input("Escribe el nuevo contenido en mililitros del producto. \n")
          contenido = int(contenido)

          cursor2 = conn.cursor()
          sql = "UPDATE producto SET contenido_mililitros = "+str(contenido)+" WHERE nombre_producto = '"+_nombre_producto+"'"
          cursor2.execute(sql)
          conn.commit()
          conn.close()
          print("El producto fue modificado exitosamente. \n")

        elif opcion == 4:
          unidades = input("Escribe el nuevo stock que tienes del producto. \n")
          while not(unidades.isnumeric()) or int(unidades) < 0:
            unidades = input("Escribe el nuevo stock que tienes del producto. \n")
          unidades = int(unidades)
          cursor2 = conn.cursor()
          sql = "UPDATE producto SET stock = " + str(unidades) + " WHERE nombre_producto = '" + _nombre_producto + "'"
          cursor2.execute(sql)
          conn.commit()
          conn.close()
          print("El producto fue modificado exitosamente. \n")

        elif opcion == 5:
          break

        editar = input(
          "Deseas modificar algún dato del producto? En caso afirmativo, presiona s. En otro caso presiona otra"
          "tecla")

    except Error as err:
      print("Ha ocurrido el error: " + str(err))
      conn.close()


  @staticmethod
  def eliminar_producto():
    print("********** Editar Producto ************\n")

    conexion = Conexion(host="localhost", port=3306, user="root", passwd="", database="licorera")
    conn = conexion.connect_database()
    cursor = conn.cursor()

    _nombre_producto = input("Por favor escribe el nombre del producto que deseas eliminar. \n")

    try:
      conn.cursor()
      sql = "DELETE FROM producto WHERE nombre_producto = '"+_nombre_producto+"'"
      cursor.execute(sql)
      conn.commit()
      conn.close()
      print("El producto fue eliminado correctamente.")

    except Error as error:
      print("Ha ocurrido el error: "+str(error))



  #buscar_producto()
  #crear_producto()



