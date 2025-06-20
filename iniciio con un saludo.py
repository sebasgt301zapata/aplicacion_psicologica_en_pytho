import datetime
nombre= input("cual es tu nombre?: ")
hora=datetime.datetime.now().hour
if hora < 12:
    print(f"buenos dias,{nombre}")
elif hora < 18:
    print(f"buenas tardes, {nombre}!")
     
else:
    print(f"buenas noches,{nombre}")

estado=input("como estas el dia de hoy")

if "bien" in estado.lower() or "bueno" in estado.lower():
    print(f"me alegra que estes bien, {nombre}")
elif "mal" in estado.lower() or "malo" in estado.lower():
    print(f"espero que te sientas mejor {nombre}")
elif "mas o menos" in estado.lower() or "no sabe como esta" in estado.lower():
    print(f"y eso porque no estas ni bien ni mal {nombre}")
elif "no se como estoy" in estado.lower() or "no sabe" in estado.lower():
    print(f"porque no sabes como estas {nombre}")
else:
    print("gracias por compartir como te sientes.")

