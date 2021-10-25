# Platzi Ventas CLI
> Platzi Ventas CLI is a project from the course "[Curso Práctico de Python: Creación de un CRUD](https://platzi.com/clases/python-practico/)" of [Platzi](https://platzi.com/).

## Table Of Contents:
 - [Description](#description)
 - [Requirements](#requirements)
 - [Installation](#installation)
 - [Usage](#basic-usage)

## Description
This application allows to create, update, list, and delete clients from a csv file.

## Requirements
- Python >= 3.6

## Installation
1. Clone or download de repository:
    ```
    $ git clone https://github.com/JoseNoriegaa/platzi-ventas-cli
    ```

2. Open the console inside the project directory and create a virtual environment.
    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

3. Install the app
    ```bash
    (venv) $ pip install .
    ```

## Basic Usage

1. List clients
    ```bash
    (venv) $ pv clients list
    ```

2. Create client
    ```bash
    (venv) $ pv clients create
    ```

3. Update client
    ```bash
    (venv) $ pv clients update -u {CLIENT_UID}
    ```

4. Delete client
    ```bash
    (venv) $ pv clients delete -u {CLIENT_UID}
    ```
