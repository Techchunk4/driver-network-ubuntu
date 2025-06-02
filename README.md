# 🚗 Driver Network Monitor - Ubuntu Edition

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)
![Ubuntu](https://img.shields.io/badge/ubuntu-24.04-e95420?logo=ubuntu)
![Flask](https://img.shields.io/badge/flask-webapp-000000?logo=flask)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight Linux-based network monitoring dashboard designed for distributed driver apps. Built with Python, Flask, and Ubuntu 24.04, it monitors domain availability and visualizes logs in a web interface.

---

## 📦 Features

- ✅ Live monitoring of website/domain status (OK / DOWN)
- 🌐 Web-based UI built with Flask
- 🖥️ Compatible with Ubuntu Desktop (no Raspberry Pi required)
- 📄 Real-time log file (`monitor_log.txt`) shown on dashboard
- ⚡ Simple, fast, and easy to deploy

---

## 📁 Folder Structure

driver-network-ubuntu/
├── monitor.py # Network/domain monitor script
├── monitor_log.txt # Output logs from monitor.py
└── web/
├── app.py # Flask web server
├── templates/
│ └── index.html # Web interface template

yaml
Copy
Edit

---

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/driver-network-ubuntu.git
   cd driver-network-ubuntu
Set up the environment:

bash
Copy
Edit
python3 -m venv env
source env/bin/activate
pip install flask
Run the domain monitor in a separate terminal:

bash
Copy
Edit
python3 monitor.py
Run the web server:

bash
Copy
Edit
cd web
python3 app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
⚙️ Configuration
Edit the list of domains to monitor inside monitor.py:

python
Copy
Edit
domains = ["google.com", "yourdomain.com", "testsite.net"]
Modify logging interval and alert threshold as needed.

📸 Screenshots
Add screenshots of your web UI here for better GitHub presentation.

🛡️ License
This project is licensed under the MIT License — see the LICENSE file for details.

🤝 Contributions
PRs and issues are welcome! If you'd like to contribute or suggest features, please open an issue or fork and submit a pull request.

📬 Contact
Built with ❤️ by Abdelkader

vbnet
Copy
Edit
