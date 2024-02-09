import os
from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = 'tu_clave_secreta'

class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta, dificultad):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.dificultad = dificultad

@app.route('/', methods=['GET', 'POST'])
def index():
    preguntas = [
    {
        'enunciado': '¿Cuál es la capital de Francia?',
        'opciones': ['Berlín', 'París', 'Londres'],
        'respuesta_correcta': 2
    },
    {
        'enunciado': '¿Cuánto es 2 + 2?',
        'opciones': ["3", "4", "5"],
        'respuesta_correcta': 2
    },
    {
        'enunciado': '¿En qué año se fundó la ONU?',
        'opciones': ["1945", "1955", "1965"],
        'respuesta_correcta': 1
    },
    {
        'enunciado': '¿Cuál es el río más largo del mundo?',
        'opciones': ["Amazonas", "Nilo", "Yangtsé"],
        'respuesta_correcta': 1
    },
    {
        'enunciado': '¿Quién escribió Cien años de soledad?',
        'opciones': ["Gabriel García Márquez", "Pablo Neruda", "Julio Cortázar"],
        'respuesta_correcta': 1
    }
    # Agrega más preguntas aquí
]
    # pregunta1 = Pregunta("¿Cuál es la capital de Francia?", ["Berlín", "París", "Londres"], 2, 1)
    # pregunta2 = Pregunta("¿Cuánto es 2 + 2?", ["3", "4", "5"], 2, 1)
    # pregunta3 = Pregunta("¿En qué año se fundó la ONU?", ["1945", "1955", "1965"], 1, 2)
    # pregunta4 = Pregunta("¿Cuál es el río más largo del mundo?", ["Amazonas", "Nilo", "Yangtsé"], 1, 2)
    # pregunta5 = Pregunta("¿Quién escribió 'Cien años de soledad'?", ["Gabriel García Márquez", "Pablo Neruda", "Julio Cortázar"], 1, 3)

    # preguntas = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5]
    pregunta = random.choice(preguntas)

    if 'pregunta_actual' not in session:
        session['pregunta_actual'] = 0

    if request.method == 'POST':
        respuesta = request.form.get('respuesta')
        if respuesta == str(preguntas[session['pregunta_actual']]['respuesta_correcta']):
            session['pregunta_actual'] += 1

    if session['pregunta_actual'] >= len(preguntas):
        return '¡Felicidades, has terminado el cuestionario!'
    else:
        pregunta = preguntas[session['pregunta_actual']]

    return render_template('index.html', pregunta=pregunta, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))