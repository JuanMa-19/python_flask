from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tareas = ["Hacer compras", "Estudiar para el examen"]

@app.route('/')
def lista_tareas():
    return render_template('tareas.html', tareas=tareas)

if __name__ == '__main__':
    app.run(debug=True)