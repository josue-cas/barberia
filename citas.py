from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario para almacenar citas
citas = []

@app.route("/")
def index():
    return render_template("index.html")  # Carga la página principal

@app.route("/agendar", methods=["POST"])
def agendar():
    # Capturamos datos enviados desde el formulario
    nombre = request.form.get("nombre")
    fecha = request.form.get("fecha")
    hora = request.form.get("hora")

    # Validamos datos básicos
    if not nombre or not fecha or not hora:
        return "Por favor completa todos los campos."

    # Guardamos la cita
    citas.append({"nombre": nombre, "fecha": fecha, "hora": hora})
    
    # Redirigimos a la página de confirmación
    return render_template("confirmacion.html", nombre=nombre, fecha=fecha, hora=hora)

if __name__ == "__main__":
    app.run(debug=True)
