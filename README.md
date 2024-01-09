# Data Network Overlock

Consola de Detección de Vulnerabilidades en Sistemas de Red.

Trabajo de grado para optar por el título de Ingenieros de Sistemas.

## Descripción

Esta es una aplicación de escritorio escrita con Python que tiene el fin de ejecutar distintos análisis sobre una red de datos para detectar las vulnerabilidades presentes en el sistema. Mediante la generación de informes pretende informar sobre el estado de la red.

## Requisitos

-   [Python 3.x](https://www.python.org/downloads/)

## Instalación de la versión de desarrollo

-   Clonación del repositorio

```bash
git clone https://github.com/DataNetworkOverlock/DNOProject
```

-   Crear entorno virtual [Ver más :bulb:](https://docs.python.org/es/3/library/venv.html)

```bash
> python -m venv my_env
> my_venv\Scripts\activate.bat
```

-   Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

-   Ejecutar

```bash
python Vistas/main.py
```

## Relacionados

Repositorio del API REST que permite la interacción de la aplicación con la base de datos para obtener información

-   [Data Network Overlock API](https://github.com/DataNetworkOverlock/dno-api#readme)
