import time
from timer import print_time, log

CLIENTS = [
    ("alice", 0.5),
    ("bob", 5.0),
    ("carol", 0.5),
    ("dave", 0.5),
    ("eve", 0.5),
]

def handle_request(client, duration):
    log(f"{client}: запрос принят")
    time.sleep(duration)
    log(f"{client}: ответ отправлен")

def main():
    for client, duration in CLIENTS:
        handle_request(client, duration)

if __name__ == "__main__":
    with print_time():
        main()