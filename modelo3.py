import random

class Pregunta:
    def __init__(self, enunciado, opciones, respuesta_correcta, dificultad):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.dificultad = dificultad

    def mostrar_pregunta(self):
        print(self.enunciado)
        for i, opcion in enumerate(self.opciones, 1):
            print(f"{i}. {opcion}")

    def verificar_respuesta(self, respuesta):
        return respuesta == self.respuesta_correcta

class EvaluacionAdaptativa:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.puntaje = 0
        self.errores = 0

    def realizar_evaluacion(self):
        for pregunta in self.preguntas:
            pregunta.mostrar_pregunta()
            respuesta = int(input("Ingresa el número de tu respuesta: "))
            
            if pregunta.verificar_respuesta(respuesta):
                print("¡Respuesta correcta!\n")
                self.puntaje += 1
            else:
                print("Respuesta incorrecta. Se generará una pregunta similar.\n")
                # Incrementar el contador de errores
                self.errores += 1
                # Generar y mostrar una pregunta similar
                pregunta_similar = self.generar_pregunta_similar(pregunta)
                pregunta_similar.mostrar_pregunta()
                respuesta_similar = int(input("Ingresa el número de tu respuesta para la pregunta similar: "))
                
                # Evaluar la respuesta similar
                if pregunta_similar.verificar_respuesta(respuesta_similar):
                    print("¡Respuesta correcta en la pregunta similar!\n")
                    self.puntaje += 1
                else:
                    print(f"Respuesta incorrecta en la pregunta similar. La respuesta correcta era la {pregunta_similar.respuesta_correcta}.\n")

        # Calcular el criterio final en base a la evaluación adaptativa
        criterio_final = self.calcular_criterio_final()
        print(f"Tu puntaje final es: {self.puntaje}/{len(self.preguntas)}")
        print(f"Total de errores: {self.errores}")
        print(f"Criterio final: {criterio_final}")

    def generar_pregunta_similar(self, pregunta):
        # Implementar lógica para generar una pregunta similar
        # Aquí puedes ajustar la dificultad, cambiar opciones, etc.
        pregunta_similar = Pregunta(
            enunciado=f"¿Cuál es una variante de la siguiente pregunta: {pregunta.enunciado}",
            opciones=pregunta.opciones,
            respuesta_correcta=pregunta.respuesta_correcta,
            dificultad=pregunta.dificultad
        )
        return pregunta_similar

    def calcular_criterio_final(self):
        # Criterio simple en base al número de aciertos y errores
        porcentaje_aciertos = (self.puntaje / len(self.preguntas)) * 100
        porcentaje_errores = (self.errores / len(self.preguntas)) * 100

        if porcentaje_aciertos >= 70:
            return "Muy bien, tienes un buen conocimiento."
        elif porcentaje_aciertos > 70 and porcentaje_errores <= 50:
            return "Tienes un conocimiento intermedio."
        else:
            return "Es posible que necesites repasar más."

def main():
    # Crear preguntas con niveles de dificultad
    pregunta1 = Pregunta("¿Cuál es la capital de Francia?", ["Berlín", "París", "Londres"], 2, 1)
    pregunta2 = Pregunta("¿Cuánto es 2 + 2?", ["3", "4", "5"], 2, 1)
    pregunta3 = Pregunta("¿En qué año se fundó la ONU?", ["1945", "1955", "1965"], 1, 2)
    pregunta4 = Pregunta("¿Cuál es el río más largo del mundo?", ["Amazonas", "Nilo", "Yangtsé"], 1, 2)
    pregunta5 = Pregunta("¿Quién escribió 'Cien años de soledad'?", ["Gabriel García Márquez", "Pablo Neruda", "Julio Cortázar"], 1, 3)

    # Mezclar preguntas para adaptar la evaluación
    preguntas = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5]
    random.shuffle(preguntas)

    # Realizar la evaluación
    evaluacion = EvaluacionAdaptativa(preguntas)
    evaluacion.realizar_evaluacion()

if __name__ == "__main__":
    main()
