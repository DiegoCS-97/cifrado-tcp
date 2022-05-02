from socket import socket

def main():
    s = socket()
    s.connect(("localhost", 6030))
    
    while True:
        f = open("captura.png", "rb")
        content = f.read(1024)
        
        while content:
            # Enviar contenido.
            s.sendall(content)
            content = f.read(1024)
        break
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        s.sendall(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))
    
    # Cerrar conexión y encriptar archivo.
    s.close()
    f.close()
    print("El archivo ha sido enviado correctamente.")
if __name__ == "__main__":
    main()