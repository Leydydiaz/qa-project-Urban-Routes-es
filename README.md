# Urban Routes Automated Testing

## 📄 Descripción del proyecto
Este proyecto implementa un conjunto de pruebas automatizadas para verificar el flujo completo de solicitud de un taxi en el sitio web de Urban Routes. Las pruebas simulan las acciones de un usuario real, incluyendo la selección de direcciones, tarifa, autenticación por teléfono, selección de extras y pago.

## 🧰 Tecnologías y técnicas utilizadas
- **Python 3**: Lenguaje principal para programar las pruebas.
- **Selenium WebDriver**: Para controlar el navegador y automatizar la interfaz web.
- **Pytest**: Framework de pruebas para ejecutar y organizar los tests.
- **Chrome DevTools Protocol (CDP)**: Para capturar y leer el código de confirmación telefónica desde las respuestas de red.
- **Espera explícita (`WebDriverWait`)**: Para garantizar la sincronización de los elementos antes de interactuar con ellos.
- **Logging**: Para depurar el proceso de prueba y registrar información útil durante la ejecución.

## 🔢 Escenario cubierto en las pruebas
1. Ingreso de dirección de origen y destino.
2. Selección de la tarifa "Comfort".
3. Ingreso y confirmación de número de teléfono mediante código.
4. Agregado de tarjeta de crédito.
5. Envio de un mensaje al conductor.
6. Solicitud de manta, pañuelos y dos helados.
7. Verificación de que las direcciones ingresadas coincidan con las esperadas.

## 📅 Estructura del proyecto
- `main.py`: Contiene las pruebas y la página de objetos (`UrbanRoutesPage`).
- `data.py`: Contiene los datos necesarios como URL, direcciones, teléfono y tarjeta.
- `README.md`: Este documento.

---

Este proyecto fue desarrollado para cumplir con las buenas prácticas de programación, uso adecuado de localizadores, modularización y cobertura total del escenario de uso descrito para Urban Routes.

