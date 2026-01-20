---

# Sorteador de Alumnos "The Chosen One"

¡Bienvenido al **Sorteador de Alumnos**! Este proyecto nació de la necesidad de dinamizar la selección de participantes en clase de una manera divertida, temática y eficiente.

##El Proyecto

Es una **Landing Page** desarrollada con Django que permite gestionar una lista de participantes y realizar sorteos aleatorios. Si eres el "elegido", el sistema te lo hará saber con una animación especial inspirada en Star Wars.

### Características principales:

* **Sorteo Inteligente**: Selección aleatoria mediante algoritmos de Python.
* **Historial en tiempo real**: Registro automático de los últimos ganadores con fecha y hora.
* **API REST**: Endpoint integrado para consultar y gestionar participantes desde aplicaciones externas.
* **Interfaz Dinámica**: Sistema de pop-ups personalizados (CSS puro) para mostrar al ganador sin errores de carga.
* **Diseño Responsivo**: Totalmente adaptado para móviles y desktop usando Bootstrap 5.

---

## Stack Tecnológico

* **Backend**: Python 3.11 & Django 5.1
* **API**: Django REST Framework (DRF)
* **Frontend**: HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5
* **Base de Datos**: SQLite3 (desarrollo)
* **Testing**: Django TestCase

---

## Desafíos Técnicos y Soluciones

En este proyecto apliqué conceptos avanzados para asegurar una experiencia de usuario profesional:

1. **Patrón PRG (Post-Redirect-Get)**: Implementé redirecciones tras el sorteo para evitar que el navegador vuelva a ejecutar el sorteo si el usuario refresca la página (F5).
2. **Gestión de Estáticos**: Optimización de carga de archivos locales (GIFs y scripts) para eliminar dependencias de servidores externos.
3. **Arquitectura de Modelos**: Relación `ForeignKey` entre Participantes y Ganadores para mantener la integridad de los datos.
4. **Tests Automatizados**: Cobertura de pruebas para la lógica de selección y los estados de respuesta HTTP.

---

## Instalación y Uso

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/sorteador.git

```


2. **Crear entorno virtual e instalar dependencias:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

```


3. **Migrar base de datos y correr servidor:**
```bash
python manage.py migrate
python manage.py runserver

```



---

## Ejecución de Pruebas

Para asegurar que todo funciona correctamente:

```bash
python manage.py test

```

---
