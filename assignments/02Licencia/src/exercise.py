def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    if edad>0:
        if edad>=18:
            identificacion=str(input("¿Tienes identificación oficial? (s/n): "))
            if identificacion=='s'or identificacion=='n':
                if edad>=18 and identificacion== 's':
                    print("Trámite de licencia concedido")
                else:
                    print("No cumples requisitos")
            else:
                print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")    
if __name__=='__main__':
    main()

