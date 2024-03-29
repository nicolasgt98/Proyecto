Nombre Proyecto: ReminderMate - Aplicación Web para gestión de recordatorios

Autor: Nicolás Garcés Toro

Correo: nicolasgt98@hotmail.com

Justificación: ReminderMate es una aplicación web diseñada para la gestión simple de recordatorios y fechas importantes

Modelos: Se crearon 4 modelos: tareas, eventos, pagos y contactos. Todos los modelos cuentan con los siguientes campos en común y con las opciones para realizar el CRUD.

(Nota: Los campos con * son obligatorios)

a. Nombre*: Permite al usuario ingresar el nombre de la tarea/pago/evento para una fácil identificación
b. Etiqueta*: Permite al usuario indicar una etiqueta para agrupar tareas/pagos/eventos
c. Recordatorio*: Permite al usuario ingresar una fecha que ayudará a gestionar tareas/pagos/eventos priorizando las fechas más próximas.
	La idea de este campo es que el usuario ingrese una fecha anterior a la fecha límite del pago/finalización de la tarea o fecha del evento para que en próximas actualizaciones de la aplicación, cada día salgan en la pantalla principal, los recordatorios según esta fecha.
d. Descripción: Permite al usuario indicar datos adicionales
		

Explicación de cada modelo

1. Tareas: En este modelo se pretende que el usuario pueda ingresar una tarea con un plazo máximo, es decir, que se puede terminar antes de esta fecha
	Fecha Límite*: Fecha máxima para completar la tarea

2. Eventos: En este modelo se pretende que el usuario pueda ingresar un evento llevado a cabo un día en específico
	Lugar*: Lugar del evento
	Fecha del Evento*: Fecha específica en la que se lleva a cabo el evento

3. Pagos:En este modelo se pretende que el usuario pueda ingresar un pago programado que se debe realizar con un plazo máximo
	Fecha Límite de Pago*: Fecha máxima para hacer el pago
	Valor*: Valor que se debe pagar
	Proveedor*: Proveedor al que se debe pagar

4. Contactos: En este modelo se pretende que el usuario pueda manejar una opción simple para guardar sus contactos con su información básica
	Apellido*: Apellido del contacto
	Correo*: Correo del contacto
	Teléfono*: Teléfono del contacto


Secciones adicionales:

1. Página Sobre Mi con información del autor

2. Página Contáctame con información de contacto del autor

3. Opción para agregar y editar perfil: Nombre, apellido y avatar

4. Ingreso, registro y cierre de sesión


Comentarios adicionales

1. Pendiente corregir el archivo "styles.css" pues no logré hacer que el css se leyera desde ahí, por lo que tuve que recurrir a agruparlo en el header del mismo archivo "home.html" (Si me pueden guiar en esta parte se los agradezco)



Usuarios:

Usuario: coderhouse
Contraseña: coder12345


Usuario: prueba2
Contraseña: nicolas123

