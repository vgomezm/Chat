
#!/usr/bin/env python

import socket

serversocket    =   socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos socket

serversocket.bind(('10.108.33.32', 8080)) #Mantenemos en esucucha el puerto (8000)

serversocket.listen(1) #Mantenemos en escucha el servidor

clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
print ('Conexion desde: ', clientaddress)  #Imprimir la IP del clientsocket
#Entra en el bucle mientras se mantenga la conexión
while 1:
        data = clientsocket.recv(1024).decode()#Recibimos los datos del cliente
        if data == "salir":
            serversocket.listen(1) #Mantenemos en escucha el servidor
            clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
            print ('Conexion desde: ', clientaddress)
        else:
            print ('El cliente dice: ', data) #Imprime los datos recibidos
            newdata = str.encode(input('>')) #Escribimos la respuesta
            clientsocket.send(newdata) #Envia la respuesta del servidor
            if newdata == str.encode("salir"):
                serversocket.listen(1) #Mantenemos en escucha el servidor
                clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
                print ('Conexion desde: ', clientaddress)

clientsocket.close() #Cierra el socket
