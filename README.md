A01420939_Pruebas_De_Software
Actividad 6.2 – Proyecto 1 (Sistema de Reservación de Hoteles)
Lenguaje utilizado: Python 3.14

Contenido y evidencias
Este repositorio contiene el código, las pruebas y la documentación solicitada para la actividad 6.2. Se incluye la siguiente estructura:

Código fuente en Python (.py): Clases principales con la lógica de negocio ubicadas en la carpeta source/ (hotel.py, customer.py, reservation.py).

Pruebas Unitarias: Casos de prueba automatizados utilizando el módulo unittest, ubicados en la carpeta tests/ (test_hotel.py, test_customer.py, test_reservation.py).

Evidencia de Linting: Capturas mostrando el análisis de calidad de código con PyLint (calificación 10/10) y Flake8 sin errores, ubicadas dentro de la carpeta results/.

Reporte de Cobertura: Archivo coverage_report.txt ubicado en la carpeta results/, el cual demuestra un 87% de cobertura de pruebas sobre el código fuente (cumpliendo con el REQ 4).

Archivos de configuración: Archivos __init__.py para la correcta importación de módulos y un .gitignore para omitir la subida de archivos de caché (__pycache__).

Observaciones
El programa cumple de manera estricta con el estándar de codificación PEP-8, validado exitosamente sin excepciones.

La persistencia de datos (creación, lectura y modificación) se maneja a través de archivos JSON. Durante la ejecución de las pruebas, los archivos temporales se generan y eliminan automáticamente (mediante setUp y tearDown) para evitar dejar residuos en el repositorio.

Se probaron satisfactoriamente los escenarios de éxito y manejo de errores (IDs duplicados, entidades inexistentes, falta de habitaciones).

Toda la evidencia presentada permite verificar la correcta ejecución, la robustez de la arquitectura del software y el cumplimiento de las especificaciones de la actividad.