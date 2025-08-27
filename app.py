from database import crear_tabla, agregar_suenio, obtener_suenios, buscar_por_palabra, buscar_por_fecha, cierra_conexion

bienvenida = """
Con esta app podremos:
1. Guardar un registro de nuestros sueños
2. Listar nuestros sueños
3. Buscar sueños recurrentes por palabra
4. Buscar sueños por fecha
5. Salir
"""

menu = """
Elige una opción:
1) Agregar un sueño
2) Listar todos los sueños
3) Buscar por palabra clave
4) Buscar por fecha
5) Salir
"""

print(bienvenida)
crear_tabla()

def pausa():
    input("\nPresiona Enter para volver al menú...")

def agrega_suenio():
    suenio = input("Escribe tu sueño: ")
    fecha = input("¿Qué día es hoy (YYYY-MM-DD)?: ")
    agregar_suenio(suenio, fecha)
    print("Sueño guardado exitosamente.")

def mostrar_lista(lista):
    if not lista:
        print("No se encontraron resultados.")
    else:
        for rowid, suenio, fecha in lista:
            print(f"[{rowid}] {suenio} ({fecha})")

while (opcion := input(menu)) != "5":
    if opcion == "1":
        agrega_suenio()
        pausa()
    elif opcion == "2":
        print("\n Tus sueños:")
        mostrar_lista(obtener_suenios())
        pausa()
    elif opcion == "3":
        palabra = input("Escribe la palabra clave: ")
        print(f"\n Resultados para '{palabra}':")
        mostrar_lista(buscar_por_palabra(palabra))
        pausa()
    elif opcion == "4":
        fecha = input("Escribe la fecha (YYYY-MM-DD): ")
        print(f"\n Sueños del día {fecha}:")
        mostrar_lista(buscar_por_fecha(fecha))
        pausa()
    else:
        print(" Opción inválida. Intenta de nuevo.")

print("CHAU")
cierra_conexion()