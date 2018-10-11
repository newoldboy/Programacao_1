import signal

def evento(*args):
    print("Evento disparado")

signal.signal(signal.SIGALRM, evento)
signal.alarm(5)

resposta = input('Por favor, aguarde 5 segundos...')