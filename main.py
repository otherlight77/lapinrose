import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dashboard = os.path.join(BASE_DIR, "ui", "dashboard.py")

subprocess.run(["python3", dashboard])
