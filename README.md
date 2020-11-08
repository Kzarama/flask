# flask

![flask](./img/flask.png)

---

Is a micro-framework, it means that seeks to make its initial infrastructure as simple as possible, and faster personalization

libraries of flask are called flask extensions

---

## To initialize a flask project

Create a file main.py

Put the decorators in the methods

Declare a new variable in the venv called FLASK_APP with the value of the main file of the instance of flask

```cmd
export FLASK_APP=main.py
```

Turn on the server

```cmd
flask run
```

### Debug

Allows that the error messages show in the browser and refresh the data in the browser

To run the server in debug mode

Create a variable called FLASK_DEBUG=1

```cmd
export FLASK_DEBUG=1
```

Another way to initialize the server in debug mode

```python
app.run(debug=True)
```
