# Tercera-pre-entrega-Geysels

El archivo models.py define la estructura de la base de datos de la aplicación, con tres modelos: Cliente, Producto y Orden. DetalleOrden es un modelo de unión entre Orden y Producto que contiene información adicional, como la cantidad y el precio unitario de un producto en una orden.

El archivo forms.py define un formulario para la creación de clientes, utilizando el modelo Cliente. El formulario asegura que los campos necesarios (nombre, apellido, correo electrónico, teléfono y dirección) estén presentes y que el correo electrónico tenga un formato válido.

La funcionalidad principal de la aplicación sería permitir a los usuarios registrarse como clientes y realizar órdenes de productos. Se podría utilizar el formulario definido en forms.py para registrar nuevos clientes y, a continuación, permitir a los usuarios agregar productos a una orden y completar la orden.
