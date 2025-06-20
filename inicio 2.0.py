import datetime

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

def conversacion():
    nombre = input("¿Cuál es tu nombre? ")
    if not nombre:
        nombre = "desconocido"
    print(saludo(nombre))

    while True:
        estado = input("¿Cómo estás? ")
        print(respuesta_estado(estado))
        accion = input("¿Quieres hablar sobre algo en particular? (sí/no): ")
        if accion.lower() == "sí":
            tema = input("¿Qué te gustaría hablar sobre? ")
            print(f"¡Genial! Hablemos sobre {tema}.")
            while True:
                comentario = input("¿Qué piensas sobre este tema? ")
                print("¡Interesante! ¿Quieres seguir hablando sobre esto?")
                seguir = input("(sí/no): ")
                if seguir.lower() != "sí":
                    break
                else:
                    print("¿Quieres agregar algo más sobre este tema?")
                    agregar = input("(si/no): ")
                    if agregar.lower() == "si":
                        comentario_adicional = input("¿Qué más quieres agregar? ")
                        print("¡Gracias por compartir!")
        else:
            print("¿Quieres saber algo en particular?")
            saber = input("(si/no): ")
            if saber.lower() == "si":
                pregunta = input("¿Qué quieres saber? ")
                print("¡Interesante pregunta! ¿Quieres que te dé una respuesta?")
                respuesta = input("(si/no): ")
                if respuesta.lower() == "si":
                    print("Lo siento, pero no tengo una respuesta específica para eso.")
                    print("¿Quieres intentar algo más?")
                else:
                    print("¡Hasta luego!")
                    break
            else:
                print("¡Hasta luego!")
                break
        continuar = input("¿Quieres seguir conversando? (si/no): ")
        if continuar.lower() != "si":
            break

conversacion()