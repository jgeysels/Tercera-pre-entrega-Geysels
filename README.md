# Tercera-pre-entrega-Geysels
http://127.0.0.1:8000/agregar_cliente/ para agregar un cliente
http://127.0.0.1:8000/buscar/ para buscar clientes, productos u ordenes por nombre
http://127.0.0.1:8000/lista_clientes/ para ver la lista de clientes
http://127.0.0.1:8000/lista_productos/ para ver la lista de productos
http://127.0.0.1:8000/lista_ordenes/ para ver la lista de órdenes

El archivo models.py define la estructura de la base de datos de la aplicación, con tres modelos: Cliente, Producto y Orden. DetalleOrden es un modelo de unión entre Orden y Producto que contiene información adicional, como la cantidad y el precio unitario de un producto en una orden.

El archivo forms.py define un formulario para la creación de clientes, utilizando el modelo Cliente. El formulario asegura que los campos necesarios (nombre, apellido, correo electrónico, teléfono y dirección) estén presentes y que el correo electrónico tenga un formato válido.


*La ultima version es la version 3.0.Aunque la versión anterior tenía más funcionalidades, también tenía algunos errores que podrían impedir que el código del proyecto funcionara correctamente. Por lo tanto, he decidido hacer algunos cambios para asegurarme de que la nueva versión sea más confiable y robusta.

Aunque la nueva versión puede ser más simple en términos de funcionalidad,el código corre perfectamente.
