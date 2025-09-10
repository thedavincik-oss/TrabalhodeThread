# Importação das bibliotecas necessárias
import threading   # Biblioteca para trabalhar com threads (execução paralela)
import time        # Biblioteca para trabalhar com tempo (pausas, contagem, etc.)
import math        # Biblioteca matemática (nesse exemplo não é usada, mas foi importada)

# Função que será executada pelas threads
def estruturaThread(nome, inicio, fim):
    """
    Essa função recebe:
    - nome: nome da thread (apenas para identificação na saída)
    - inicio: número inicial da contagem
    - fim: número final da contagem
    A função vai imprimir os números de inicio até fim,
    com uma pausa de 10 segundos entre cada impressão.
    """
    for i in range(inicio, fim + 1):  # percorre os números de inicio até fim
        print(f"{nome} -> {i}")       # imprime o nome da thread e o número atual
        time.sleep(3)                # pausa de 10 segundos entre cada número

# Criação da primeira thread
# Vai imprimir apenas o número 3
thread1 = threading.Thread(target=estruturaThread, args=("thread1", 3, 30))

# Criação da segunda thread
# Vai imprimir os números de 40 até 70
thread2 = threading.Thread(target=estruturaThread, args=("thread2", 40, 70))

# Início da execução das duas threads em paralelo
thread1.start()
thread2.start()
