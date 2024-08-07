# Proyecto Integrador Backend: Tienda de Mascotas

## Equipo de Desarrollo - Grupo 3

- Damian Perez - [https://github.com/DamianGPerez](https://github.com/DamianGPerez)
- Javier Salguero - [https://github.com/JavierSalguero](https://github.com/JavierSalguero)
- Juan Rodriguez - [https://github.com/juan25165](https://github.com/juan25165)
- Ricardo Nicolas Gomez Granillo - [https://github.com/RicardoN7](https://github.com/RicardoN7)

## Descripción

Se integra el [Proyecto Frontend](https://github.com/JavierSalguero/Proyecto-Final-Grupo-3.github.io) al Backend desarrollado mediante el uso del framework Flask en la segunda etapa del curso. El sitio creado en la primera etapa se trataba de una **web responsive** sobre una Tienda de Mascotas.
 [Deploy del Proyecto Frontend](https://damiangperez.github.io/DamianGPerez-Codo-Codo-4.1-Proyecto-Final/)

## Instrucciones para trabajar con el proyecto localmente

1. Crear la carpeta que contendrá el proyecto y el entorno virtual
2. Forkear el proyecto y luego clonarlo con: `git clone url-proyecto-forkeado` dentro de dicha carpeta
3. Abrir una **terminal command prompt**, ubicarse en la carpeta creada y preparar el entorno virtual: `python -m venv nombre-del-entorno`
4. Ingresar a la carpeta del entorno y luego al sub-directorio Scripts para activarlo:
   `cd nombre-del-entorno`
   `cd Scripts`
   `activate `
5. Regresar a la primer carpeta con `cd..`
6. Instalar Flask: `pip install Flask`
7. Instalar blinker: `pip install blinker`
8. Instalar click: `pip install click`
9. Instalar colorama: `pip install colorama`
10. Instalar itsdangerous: `pip install itsdangerous`
11. Instalar Jinja2: `pip install Jinja2`
12. Instalar MarkupSafe: `pip install MarkupSafe`
13. Instalar PyMySQL: `pip install PyMySQL`
14. Instalar Werkzeug: `pip install Werkzeug`
15. Para **ejecutar el servidor** ingresar a la carpeta del proyecto y tipear: `python manage.py runserver` si queremos **detener el servidor** presionamos _Ctrol + C_ y si deseamos **detener el entorno virtual**, hay que escribir: `deactivate` desde cualquier carpeta.

## Requisitos

- blinker==1.8.2
- click==8.1.7
- colorama==0.4.6
- Flask==3.0.3
- itsdangerous==2.2.0
- Jinja2==3.1.4
- MarkupSafe==2.1.5
- PyMySQL==1.1.1
- Werkzeug==3.0.3

---

### Consignas solicitadas

- [x] La base de datos debe desarrollarse en lenguaje SQL
- [x] A través del front se debe poder realizar al menos un tipo de alta (POST)
- [x] De la misma forma se debe poder realizar modificaciones de los registros
- [x] Se debe poder acceder a los registros de la tabla (GET)
- [x] Se debe poder realizar borrado físico de los datos (DELETE)
- [x] El trabajo práctico deberá subirse a un servidor online y compartirse mediante un repositorio de Git (Obligatorio)
- [x] La página deberá subirse a un servidor on-line para poder ser navegada (Obligatorio)
- [x] El backend debe estar integrado con un frontend
