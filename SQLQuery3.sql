--CREATE PROCEDURE sp_BuscarLibroPorTitulo
--    @Titulo NVARCHAR(255)
--AS
--BEGIN
--    SET NOCOUNT ON;

--    SELECT 
--        titulo,
--        isbn,
--        paginas,
--        editorial
--    FROM 
--        Biblioteca.Libro
--    WHERE 
--        titulo = @Titulo;
--END;

--EXEC sp_BuscarLibroPorTitulo @Titulo = 'Rayuela';

--CREATE PROCEDURE sp_InsertarPrestamoLibros
--@codigo_usuario INT,
--@codigo_ejemplar INT

--AS 
--BEGIN
--SET NOCOUNT ON;

--INSERT INTO BIBLIOTECA.USUARIO_EJEMPLAR(CODIGO_USUARIO, CODIGO_EJEMPLAR,FECHA_PRESTAMO, FECHA_DEVOLUCION)
--VALUES (@codigo_usuario, @codigo_ejemplar, GETDATE(), '2024-09-25')

--END;

--EXEC sp_InsertarPrestamoLibros @codigo_usuario= '27', @codigo_ejemplar='32'

--CREATE PROCEDURE sp_Actualizar
--@nombre VARCHAR (25),
--@codigo INT


--AS
--BEGIN
--SET NOCOUNT ON;
--UPDATE BIBLIOTECA.AUTOR
--SET NOMBRE= @nombre
--WHERE CODIGO= @codigo
--END

--GO
--SELECT *FROM BIBLIOTECA.AUTOR
--EXEC sp_Actualizar @nombre= 'Valery Barboza', @codigo= 1

--ALTER TABLE BIBLIOTECA.USUARIO_EJEMPLAR
--ADD CONSTRAINT FK_USUARIO_EJEMPLAR
--FOREIGN KEY (CODIGO_USUARIO) REFERENCES BIBLIOTECA.USUARIO (codigo_usuario)
--ON DELETE CASCADE 

CREATE PROCEDURE sp_Eliminar
@codigo_usuario INT

AS 
BEGIN
SET NOCOUNT ON;

DELETE FROM.BIBLIOTECA.USUARIO
WHERE CODIGO_USUARIO= @codigo_usuario

END 
GO

EXEC sp_Eliminar @codigo_usuario = 1

SELECT *FROM BIBLIOTECA.USUARIO
