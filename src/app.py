from flask import Flask, render_template, request, redirect, url_for
import os
import conexion as db  # importamos la conexión


# Obtener el directorio de templates personalizado
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

# Inicializar la app Flask con el path de las plantillas
app = Flask(__name__, template_folder=template_dir)

# Ruta de la aplicacion
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall() #La información viene como tupla y se debe convertir a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
        cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar usuarios en la Bd
@app.route('/user', methods=['POST'])
def addUser():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if name and email and password:
        cursor = db.database.cursor()
        sql = "INSERT INTO users (name, email, password) VALUES(%s, %s, %s)"
        data = (name, email, password)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

#Ruta para borrar usuarios en la Bd
@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql="DELETE FROM users WHERE id = %s "
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

#Ruta para editar usuarios en la Bd
@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    if name and email and password:
        cursor = db.database.cursor()
        sql="UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s"
        data = (name, email, password, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=False, port=4000)
