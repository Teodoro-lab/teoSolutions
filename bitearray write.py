from os import strerror



try:
    bf = open('file.bin', 'rb')
    print(bf)


except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))
