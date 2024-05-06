import os
import signal
import sys
import time

CHILD_COUNT = 3

def signal_handler(signum, frame):
    if signum == signal.SIGINT:
        print(f"Получен сигнал SIGINT (Ctrl+C). Завершение процесса PID: {os.getpid()}...")
        sys.exit(0)
    elif signum == signal.SIGTERM:
        print(f"Получен сигнал SIGTERM. Завершение процесса PID: {os.getpid()}...")
        sys.exit(0)
    else:
        print(f"Получен сигнал {signum}. Игнорирование...")

def child_process():
    print(f"Дочерний процесс с PID={os.getpid()} запущен.")
    while True:
        time.sleep(1)
        if(os.getppid() == 1):
            print(f"Процесс зомби PID: {os.getpid()} завершен.")
            break

if __name__ == "__main__":
    # Регистрация обработчиков сигналов
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    child_pid = -1
    # Создание дочерних процессов

    for i in range (CHILD_COUNT) : 
        print("Процесс ", i)
        child_pid = os.fork()
        match child_pid:
            case -1:
                eprint("fork")
                os.exit(-1)
            case 0:
                child_process()
                break;
            case _:
                print(f"Родительский процесс с PID={os.getpid()} запущен.")
                print("Нажмите Ctrl+C или отправьте сигнал SIGTERM для завершения программы.")

    if(child_pid > 0):
        for w in range(CHILD_COUNT):
            os.waitpid(-1, 0)