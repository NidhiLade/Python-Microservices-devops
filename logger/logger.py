import time, json

LOG_FILE = "logs.txt"

def log_message(msg):
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps({"log": msg, "time": time.time()}) + "\n")

if __name__ == "__main__":
    while True:
        log_message("Logger service running...")
        time.sleep(5)