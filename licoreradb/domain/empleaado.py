
from domain.conexiondb import Conexion
from domain.producto import producto

class empleado:

  def __init__(self, nombre, usuario, clave):
    self._nombre = nombre
    self._usuario = usuario
    self._clave = clave


  @property
  def nombre(self):
    return self._nombre

  @nombre.setter
  def nombre(self, nombre):
    self._nombre = nombre

  @property
  def usuario(self):
    return self._usuario

  @usuario.setter
  def usuario(self, usuario):
    self._usuario = usuario

  @property
  def clave(self):
    return self._clave

  @clave.setter
  def clave(self, clave):
    self._clave = clave

  @staticmethod
  def login():
    print("************ Login LicoExpress ************ \n")

    _usuario = input("Por favor escribe tu usuario. \n")
    _clave = input("Por favor escribe tu clave. \n")

    conexion = Conexion(host="localhost", port=3306, user="root", passwd="", database="licorera")
    conn = conexion.connect_database()
    cursor = conn.cursor()
    sql = "SELECT usuario, clave FROM empleado"
    cursor.execute(sql)
    filas = cursor.fetchall()

    validacion = "por confirmar"

    for i in range(0, len(filas)):
      if filas[i][0] == _usuario and filas[i][1] == _clave:
        validacion = "confirmado"
    if validacion == "confirmado":
      print("************ Bienvenido a LicoExpress ************ \n")

      opcion = input("Por favor escribe: \n"
                     "1. Si deseas crear un producto. \n"
                     "2. Si deseas consultar un producto. \n"
                     "3. Si deseas actualizar un producto. \n"
                     "4. Si deseas eliminar un producto. \n"
                     "5. Si deseas salir. \n")

      while not(opcion.isnumeric()) or int(opcion) < 0 or int(opcion) >= 6:
        opcion = input("Por favor escribe: \n"
                       "1. Si deseas crear un producto. \n"
                       "2. Si deseas consultar un producto. \n"
                       "3. Si deseas actualizar un producto. \n"
                       "4. Si deseas eliminar un producto. \n"
                       "5. Si deseas salir. \n")
      opcion = int(opcion)

      while opcion >= 1 and opcion <=5:
        if opcion == 1:
          producto.crear_producto()
          opcion = input("Por favor escribe: \n"
                         "1. Si deseas crear un producto. \n"
                         "2. Si deseas consultar un producto. \n"
                         "3. Si deseas actualizar un producto. \n"
                         "4. Si deseas eliminar un producto. \n"
                         "5. Si deseas salir. \n")

          while not (opcion.isnumeric()) or int(opcion) < 0 or int(opcion) >= 6:
            opcion = input("Por favor escribe: \n"
                           "1. Si deseas crear un producto. \n"
                           "2. Si deseas consultar un producto. \n"
                           "3. Si deseas actualizar un producto. \n"
                           "4. Si deseas eliminar un producto. \n"
                           "5. Si deseas salir. \n")
          opcion = int(opcion)

        elif opcion == 2:
          producto.buscar_producto()
          opcion = input("Por favor escribe: \n"
                         "1. Si deseas crear un producto. \n"
                         "2. Si deseas consultar un producto. \n"
                         "3. Si deseas actualizar un producto. \n"
                         "4. Si deseas eliminar un producto. \n"
                         "5. Si deseas salir. \n")

          while not (opcion.isnumeric()) or int(opcion) < 0 or int(opcion) >= 6:
            opcion = input("Por favor escribe: \n"
                           "1. Si deseas crear un producto. \n"
                           "2. Si deseas consultar un producto. \n"
                           "3. Si deseas actualizar un producto. \n"
                           "4. Si deseas eliminar un producto. \n"
                           "5. Si deseas salir. \n")
          opcion = int(opcion)

        elif opcion == 3:
          producto.editar_producto()
          opcion = input("Por favor escribe: \n"
                         "1. Si deseas crear un producto. \n"
                         "2. Si deseas consultar un producto. \n"
                         "3. Si deseas actualizar un producto. \n"
                         "4. Si deseas eliminar un producto. \n"
                         "5. Si deseas salir. \n")

          while not (opcion.isnumeric()) or int(opcion) < 0 or int(opcion) >= 6:
            opcion = input("Por favor escribe: \n"
                           "1. Si deseas crear un producto. \n"
                           "2. Si deseas consultar un producto. \n"
                           "3. Si deseas actualizar un producto. \n"
                           "4. Si deseas eliminar un producto. \n"
                           "5. Si deseas salir. \n")
          opcion = int(opcion)
        elif opcion == 4:
          producto.eliminar_producto()
          opcion = input("Por favor escribe: \n"
                         "1. Si deseas crear un producto. \n"
                         "2. Si deseas consultar un producto. \n"
                         "3. Si deseas actualizar un producto. \n"
                         "4. Si deseas eliminar un producto. \n"
                         "5. Si deseas salir. \n")

          while not (opcion.isnumeric()) or int(opcion) < 0 or int(opcion) >= 6:
            opcion = input("Por favor escribe: \n"
                           "1. Si deseas crear un producto. \n"
                           "2. Si deseas consultar un producto. \n"
                           "3. Si deseas actualizar un producto. \n"
                           "4. Si deseas eliminar un producto. \n"
                           "5. Si deseas salir. \n")
          opcion = int(opcion)

        elif opcion == 5:
          print("Has seleccionado salir. Vuelve pronto. \n")
          opcion = 6
          empleado.login()
    else:
      print("Credenciales incorrectas. \n")
      empleado.login()

  #login()






