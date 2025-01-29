import requests
import time
import os
import tkinter as tk
import threading

url = "http://127.0.0.1:8080/scores"  # Insert IPv4 Address of Host, Use http://127.0.0.1:8080/scores for same system

file_path = os.path.join(os.path.dirname(__file__), "scores.txt")# Installation Path

interval = 10  # Interval in seconds

def download_file():
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, "wb") as file:
                file.write(response.content)
            print("File downloaded successfully!")
        else:
            print("Failed to download the file.")
        time.sleep(interval)

def start_gui():
    root = tk.Tk()
    root.title("Request Status")
    root.geometry("400x200")
    root.configure(bg='black')

    label_status = tk.Label(root, text="Requests running...", fg="white", bg="black", font=("Helvetica", 12))
    label_status.pack(pady=10)

    label_url = tk.Label(root, text=f"URL: {url}", fg="white", bg="black", font=("Helvetica", 12))
    label_url.pack(pady=10)

    label_interval = tk.Label(root, text=f"Interval: {interval} seconds", fg="white", bg="black", font=("Helvetica", 12))
    label_interval.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    request_thread = threading.Thread(target=download_file)
    request_thread.daemon = True
    request_thread.start()

    start_gui()

