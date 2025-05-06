# Urban Routes Automated Testing 📄

## Descripción del proyecto
Este proyecto implementa un conjunto de pruebas automatizadas para verificar el flujo completo de solicitud de un taxi en el sitio web de Urban Routes. Las pruebas simulan las acciones de un usuario real, incluyendo la selección de direcciones, tarifa, autenticación por teléfono, selección de extras y pago.

## Tecnologías y técnicas utilizadas
- **Python 3**: Lenguaje principal para programar las pruebas.
- **Selenium WebDriver**: Para controlar el navegador y automatizar la interfaz web.
- **Pytest**: Framework de pruebas para ejecutar y organizar los tests.
- **Chrome DevTools Protocol (CDP)**: Para capturar y leer el código de confirmación telefónica desde las respuestas de red.
- **Espera explícita (WebDriverWait)**: Para garantizar la sincronización de los elementos antes de interactuar con ellos.
- **Logging**: Para depurar el proceso de prueba y registrar información útil durante la ejecución.

## Escenario cubierto en las pruebas
- Ingreso de dirección de origen y destino.
- Selección de la tarifa "Comfort".
- Ingreso y confirmación de número de teléfono mediante código.
- Agregado de tarjeta de crédito.
- Envío de un mensaje al conductor.
- Solicitud de manta, pañuelos y dos helados.
- Verificación de que las direcciones ingresadas coincidan con las esperadas.
- Validación de que el modelo de coche buscado aparezca en los resultados.

## Estructura del proyecto
- **main.py**: Contiene las pruebas y la clase `UrbanRoutesPage`.
- **data.py**: Contiene los datos necesarios como URL, direcciones, teléfono y tarjeta.
- **README.md**: Este documento.

## Información del desarrollador
- **Nombre completo**: Leydy Mayerly Diaz Martinez
- **Cohorte**: 25

## Instrucciones para ejecutar las pruebas

### Requisitos previos:
1. Tener instalado **Python 3**.
2. Tener instalado **Google Chrome** y el controlador **ChromeDriver** compatible.

### Instalar las dependencias del proyecto:
```bash

pip install selenium pytest
Ejecutar las pruebas:
Desde la raíz del proyecto, ejecuta el siguiente comando:
pytest main.py
O, si prefieres especificar la ubicación del archivo de pruebas, usa:

bash
Copiar
Editar
pytest folder/del/proyecto/tests.py
Pruebas implementadas
Las pruebas cubren los siguientes casos:

test_set_route: Verifica que se pueda establecer una ruta correctamente.

test_select_plan: Comprueba que la selección del plan funcione como se espera.

test_fill_phone_number: Valida que el número de teléfono pueda ser ingresado correctamente.

test_fill_card: Asegura que los datos de tarjeta se ingresen y validen correctamente.

test_comment_for_driver: Verifica que se pueda agregar un comentario para el conductor.

test_order_blanket_and_handkerchiefs: Confirma que se puedan pedir mantas y pañuelos.

test_order_2_ice_creams: Verifica que se puedan agregar dos helados al pedido.

test_car_search_model_appears: Valida que el modelo de coche buscado aparezca en los resultados.

Notas
Asegúrate de tener el ChromeDriver compatible con tu versión de Google Chrome.

Puedes cambiar los datos de prueba en el archivo data.py si es necesario.
