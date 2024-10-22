from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "tu_clave_secreta"  # Cambia esta clave para proteger las sesiones

# Diccionario simulado de usuarios con nombre de usuario y contraseñas
usuarios = {
    "flores": "1234",  # Ejemplo basado en el contexto
    "admin": "adminpass"
}

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('bienvenido'))  # Redirigir a la página de bienvenida si está logueado
    return redirect(url_for('login'))  # Si no está logueado, redirigir a login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre_usuario = request.form['usuario']
        contrasena = request.form['password']
        
        # Verifica si el usuario existe y si la contraseña es correcta
        if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
            session['usuario'] = nombre_usuario  # Guarda el nombre de usuario en la sesión
            flash('Has iniciado sesión correctamente', 'success')
            return redirect(url_for('bienvenido'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

@app.route('/bienvenido')
def bienvenido():
    if 'usuario' not in session:
        flash('Debes iniciar sesión para ver esta página', 'warning')
        return redirect(url_for('login'))

    return render_template('welcome.html', usuario=session['usuario'])

@app.route('/logout')
def logout():
    session.pop('usuario', None)  # Elimina la información de la sesión
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
