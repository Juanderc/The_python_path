from multiprocessing import Process, current_process
import os


def saludo(n):
    print("---------------------------")
    name = current_process().name
    print(name, 'Saludo')
    print("hola {}".format(n))
    print("Parent id {}" .format(os.getppid()))
    print("Process id {}" .format(os.getpid()))
    print("---------------------------\n")


def main():
    # Toma la funcion como objetivo y le pasa los parametros mediante args
    p1 = Process(target=saludo, args=('Jose',)).start()

    p2 = Process(target=saludo, args=('Pedro',)).start()

    p3 = Process(target=saludo, args=('Maria',)).start()

    # Este atributo hace que se espere a la conclucion de los demas procesos

    p1.join()
    p2.join()
    p3.join()

    # Determina si el proceso aun se esta ejecutando
    print(f'Proces p is alive: {p1.is_alive()}')


if __name__ == '__main__':
    main()
