import os
import time
import subprocess
from datetime import datetime

def check_ping(host):
    """Check host connectivity using ping"""
    try:
        subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", host],
            stderr=subprocess.STDOUT
        )
        return True
    except subprocess.CalledProcessError:
        return False

def play_alert():
    """Play audio alert with error handling"""
    try:
        subprocess.run(
            ["play", "-n", "synth", "0.3", "sine", "880"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass  # Silently fail if play command fails or isn't available

log_file = "monitor_log.txt"

# Clear previous log file to prevent stale data
open(log_file, "w").close()

try:
    while True:
        print("%Checking connectivity...")
        try:
            with open("targets.txt", "r") as f:
                targets = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("Error: targets.txt not found")
            targets = []

        for host in targets:
            status = "OK" if check_ping(host) else "DOMN"  # Use DOMN here
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"{now} - {host} - {status}"

            print(message)
            with open(log_file, "a") as log:
                log.write(message + "\n")
                log.flush()  # Force immediate write

            if status == "DOMN":
                play_alert()

        time.sleep(10)

except KeyboardInterrupt:
    print("\nMonitoring stopped")