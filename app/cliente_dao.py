from cliente import Cliente
from conexion import Conexion



class ClienteDAO:
    SELECIONAR = 'SELECT * FROM cliente'
    SELECCIONAR_ID = 'SELECT * FROM cliente WHERE id=%s'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar_por_id(cls, id):
        conexion= None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            #Mapeo de clase - tabla cliente
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f'Ocurrio un error al seleccionar cliente por id: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion =  Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECIONAR)
            registros = cursor.fetchall()
            #Mapeo de clase - tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod 
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores= (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
              print(f'Ocurrio un error al actualizar clientes: {e}')
        finally:
              if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    #Insertar
    #cliente1= Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    #clientes_insertados = ClienteDAO.insertar(cliente1)
    #print(f'Clientes insertados: {clientes_insertados}')

    #Actualización
    #cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    #clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    #print(f'Clientes actualizados: {clientes_actualizados}')

    #Eliminar cliente
    #cliente_eliminar = Cliente(id=3)
    #clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    #print(f'Clientes eliminados: {clientes_eliminados}')

    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
      print(cliente)


            