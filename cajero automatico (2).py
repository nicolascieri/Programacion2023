print ("INGRESO AL SISTEMA")
monto=10000
user=input("ingrese su nombre de usuario: ")
contra=int (input("ingrese su contraseña: "))
while True:
    if user!="nico" and contra!=1234:
        print("Ingreso exitoso.")
        break
    else: 
        print("Acceso denegado. Intente nuevamente.")
        break
print("1- EXTRACCION")
print("2- DEPOSITO")

accion=input("Seleccione la operacion que desee realizar: ")
if accion=="1" and monto>=0:
    extraccion=int (input("Ingrese el monto que desea extraer: "))
    fondos=monto-extraccion
    print("Extraccion exitosa")
    print("Sus fondos: ", fondos)
else:
    deposito=int (input("Ingrese el monto que desea depositar: "))
    fondos=monto+deposito
    print("Deposito exitoso")
    print("Sus fondos: ", fondos)