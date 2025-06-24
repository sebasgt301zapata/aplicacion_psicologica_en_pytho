import datetime

# Diccionario con preguntas y respuestas
preguntas_respuestas = {
    "¿Qué es el clima?": "El clima se refiere a las condiciones atmosféricas promedio en un lugar determinado.",
    "¿Qué es la inteligencia artificial?": "La inteligencia artificial es un campo de la informática que se enfoca en crear sistemas capaces de realizar tareas que requieren inteligencia humana.",
    "¿Qué es el aprendizaje automático?": "El aprendizaje automático es un subcampo de la inteligencia artificial que se enfoca en crear algoritmos que pueden aprender de los datos.",
}

def saludo(nombre):
    hora = datetime.datetime.now().hour
    if hora < 12:
        return f"Buenos días, {nombre}!"
    elif hora < 18:
        return f"Buenas tardes, {nombre}!"
    else:
        return f"Buenas noches, {nombre}!"

def respuesta_estado(estado):
    if "bien" in estado.lower() or "bueno" in estado.lower():
        return "Me alegra que estés bien!"
    elif "mal" in estado.lower() or "malo" in estado.lower():
        return "Espero que te sientas mejor pronto."
    else:
        return "Gracias por compartir cómo te sientes."

def respuesta_pregunta(pregunta):
    if pregunta in preguntas_respuestas:
        return preguntas_respuestas[pregunta]
    else:
        return "Lo siento, pero no tengo una respuesta específica para eso."

def conversacion():
    nombre = input("¿Cuál es tu nombre? ")
    if not nombre:
        nombre = "desconocido"
    print(saludo(nombre))

    while True:
        estado = input("¿Cómo estás? ")
        print(respuesta_estado(estado))
        accion = input("¿Quieres hablar sobre algo en particular o hacer una pregunta? (hablar/pregunta): ")
        if accion.lower() == "hablar":
            tema = input("¿Qué te gustaría hablar sobre? ")
            print(f"¡Genial! Hablemos sobre {tema}.")
            while True:
                comentario = input("¿Qué piensas sobre este tema? ")
                print("¡Interesante! ¿Quieres seguir hablando sobre esto?")
                seguir = input("(sí/no): ")
                if seguir.lower() != "sí":
                    break
        elif accion.lower() == "pregunta":
            pregunta = input("¿Qué quieres saber? ")
            print(respuesta_pregunta(pregunta))
        else:
            print("¡Hasta luego!")
            break
        continuar = input("¿Quieres seguir conversando? (sí/no): ")
        if continuar.lower() != "sí":
            break

conversacion()