# SauceDemo Automation Framework

Este proyecto es un framework de automatización E2E construido con Python, Selenium y Pytest, siguiendo el patrón Page Object Model (POM). La idea es tener una base clara, escalable y fácil de mantener para pruebas automatizadas.

🚀 ¿Qué incluye?

Arquitectura POM: Separación limpia entre la lógica de negocio y los selectores. Esto hace que el código sea más ordenado y mantenible.
Waits explícitos: No se utiliza time.sleep. Lo que utilice son esperas explícitas para lograr mayor estabilidad en los tests.
Gestión automática de drivers: Gracias a webdriver-manager, no hace falta descargar ni configurar binarios manualmente.
Reportes: Generación de reportes en HTML.
Screenshots automáticos: Si un test falla, se captura pantalla automáticamente para facilitar el análisis.
Configuración flexible: Uso de variables de entorno para definir URL, credenciales y otros datos sensibles.

## 🛠️ Tecnologías
- Python 3.9+
- Selenium WebDriver
- Pytest
- Allure Report
- GitHub Actions (CI/CD)

## 📦 Instalación
1. Clonar repositorio.
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno y instalar dependencias: `pip install -r requirements.txt`
4. Configurar `.env`

## ▶️ Ejecución
- Ejecutar todos los tests: `pytest`
- Ejecutar con reportes HTML: `pytest --html=reports/report.html`
- Ejecutar con Allure: `pytest --alluredir=./allure-results` y luego `allure serve`

## 🤖 CI/CD
Este proyecto incluye un workflow de GitHub Actions para ejecutar las pruebas en cada push a la rama main.