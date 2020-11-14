# flask

![flask](./img/flask.png)

---

Is a micro-framework, it means that seeks to make its initial infrastructure as simple as possible, and faster personalization

libraries of flask are called flask extensions

---

## To install flask

```cmd
pip install flask
```

## To initialize a flask project

Create a file main.py

Put the decorators in the methods

Declare a new variable in the venv called FLASK_APP with the value of the main file of the instance of flask

### In windows

```cmd
set FLASK_APP=main.py
```

### In linux

```cmd
export FLASK_APP=main.py
```

Turn on the server

```cmd
flask run
```

## Templates of flask

Create a folder called templates and add the html files here, in the py file import render_template from flask and return the render_template with the name of the template like parameter.

For use parameters pass the variable in the render template in the py file and in the html file add with NAME_OF_VARIABLE replaced for the name of the variable of the py file

```html
{{ NAME_OF_VARIABLE }}
```

### Control structures in html file

#### If

```html
{% if %} ... {% else %} ... {% endif %}
```

#### for

```html
{% for x in range() %} ... {% endfor %}
```

### Extends templates

To extend the base html file (child component)

```html
{% extends 'base.html' %}
```

Create a block to insert the code in the base, use {{ super() }} to don't overwrite the content of the father (child component)

```html
{% block NAME_BLOCK %}{{ super() }}...{% endblock %}
```

In the father component indicate where the child component have to render

```html
{% block NAME_BLOCK %}{% endblock %}
```

### Macros

Code that can be invoked with a key work in anywhere

Create the macro.html file

```html
{% macro NAME_MACRO(PARAMETERS) %} ... {% endmacro %}
```

In the place to be used import the macros

```html
{% import 'macros.html' as macros %}
```

And invoke the macro with

```html
{{ macros.NAME_MACRO(PARAMETERS) }}
```

### Include html code

To include html code in another file create a html file with the code and in the place to be included the code add

```html
{% include 'NAME_FILE.html' %}
```

## Debug

Allows that the error messages show in the browser and refresh the data in the browser

To run the server in debug mode

Create a variable called FLASK_DEBUG=1

### In windows

```cmd
set FLASK_ENV=development
```

### In linux

```cmd
export FLASK_DEBUG=1
```

Another way to initialize the server in debug mode

```python
app.run(debug=True)
```
