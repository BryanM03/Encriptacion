import msvcrt
from cryptography.fernet import Fernet


palabra_encriptar = input("Ingrese Contraseña a Encriptar:")

encri = Fernet.generate_key()
encriptado = Fernet(encri)
palabra_encriptada = encriptado.encrypt(str.encode(palabra_encriptar))
print ("Contraseña Encriptada" )
print ( palabra_encriptada)

textodesencriptado = input("Ingrese Contraseña a Encriptar:")

textodesencriptado = encriptado.decrypt(palabra_encriptada)
print(textodesencriptado)

msvcrt.getch()