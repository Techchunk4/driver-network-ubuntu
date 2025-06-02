from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

# Define absolute path to log file
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../monitor_log.txt")

def get_logs():
    """Read and parse log file with error handling"""
    try:
        with open(LOG_FILE, 'r') as f:
            logs = []
            for line in f.readlines():
                parts = line.strip().split(' - ')
                if len(parts) == 3:
                    timestamp, host, status = parts
                    logs.append({
                        'timestamp': timestamp,
                        'host': host,
                        'status': status,
                        'is_ok': status == 'OK'
                    })
            return logs
    except Exception as e:
        print(f"Error reading log file: {str(e)}")
        return []

@app.route("/")
def dashboard():
    logs = get_logs()[-15:]  # Get last 15 entries
    status_counts = {
        'OK': sum(1 for log in logs if log['status'] == 'OK'),
        'DOMN': sum(1 for log in logs if log['status'] == 'DOMN')
    }
    
    return render_template(
        "index.html",
        logs=reversed(logs),  # Newest first
        total_hosts=len({log['host'] for log in logs}),
        ok_count=status_counts['OK'],
        down_count=status_counts['DOMN'],
        last_updated=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

if __name__ == "__main__":
    print(f"Monitoring log file at: {LOG_FILE}")
    app.run(debug=True, host="0.0.0.0", port=5000)