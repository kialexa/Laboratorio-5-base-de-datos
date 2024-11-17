import pyodbc

def connect_to_sql_server():
    server = 'LAPTOP-UA947PGB'
    database = 'IF4100_BIBLIOTECA'
    username = 'valery'
    password = '123456'

    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        connection = pyodbc.connect(conn_str)
        print("Connection established successfully\n")
        return connection
    except pyodbc.Error as e:
        print(f"Connection failed: {e}")
        return None

def probarConexion():
    connection = connect_to_sql_server()   
    if connection:
        cursor = connection.cursor()
        eleccionBD(cursor)
        connection.close()
    else:
        print("No se pudo establecer la conexión.")

def eleccionBD(cursor):
    eleccion = input('Qué deseas realizar\n1: Consultar Libro\n2: Actualizar Autor\n3: Borrar Estudiante\n4: '
                     'Insertar prestamo\n')
    if int(eleccion) == 1:
        consultarLibro(cursor);
    elif int(eleccion) == 2:
        actualizarAutor(cursor);
    elif int(eleccion) == 3:
        borrarEstudiante(cursor);
    elif int(eleccion) == 4:
        insertarPrestamo(cursor);
    else:
        print('No es un valor valido');

def consultarLibro(cursor):
    nombreProcedimiento = 'sp_BuscarLibroPorTitulo'
    titulo = input('Inserta el título del libro \n')
    cursor.execute(f"EXEC {nombreProcedimiento} ?", (titulo,))
    imprimirResultados(cursor.fetchall())

def actualizarAutor(cursor):
    nombreProcedimiento='sp_Actualizar';
    nombre=input('Inserte el nuevo nombre\n');
    codigo=input('Inserte el codigo del Autor\n');
    cursor.execute(f"EXEC {nombreProcedimiento} ?, ?", (nombre,int(codigo),));
    cursor.connection.commit()  # Confirmar los cambios en la base de datos
    print('El autor ha sido actualizado correctamente con el nombre '+nombre+' y codigo: '+codigo);

def imprimirResultados(resultados):
    for resultado in resultados:
        print(resultado)

def borrarEstudiante(cursor):
    nombreProcedimiento='sp_Eliminar';
    codigo=input('Inserte el codigo del usuario que desea eliminar: \n');
    cursor.execute(f"EXEC {nombreProcedimiento} ?", (int(codigo),));
    cursor.connection.commit()  # Confirmar los cambios en la base de datos 
    input('Se ha eliminado correctamente al estudiante con el codigo: '+codigo);

def insertarPrestamo(cursor):
    nombreProcedimiento='sp_InsertarPrestamoLibros';
    codigoUsuario=input('Ingrese el código del usuario al que asignara el prestamo\n');
    codigoEjemplar=input('Ingrese el código del ejemplar\n');
    cursor.execute(f"EXEC {nombreProcedimiento} ?, ?", (int(codigoUsuario),int(codigoEjemplar),));
    cursor.connection.commit()  # Confirmar los cambios en la base de datos 
    print('Se insertó un prestamo al usuario: '+codigoUsuario+' con el ejemplar: '+codigoEjemplar);

probarConexion();