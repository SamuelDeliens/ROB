import socket
HOST= '192.168.0.10'
PORT= 6781

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print ('connexion vers' + HOST + ':' + str(PORT) + 'reussie.')


message= 'GETLDATA'
n=client.send(str.encode(message))
print ('envoi de :' + message)
if (n != len(message)):
    print ('erreur envoi')
else :
    print ('envoi ok.')
donnees = client.recv(4096)   
print( 'Reception...')
print (donnees)
print ('Deconnexion')
client.close()