from bottle import Bottle, static_file, template
import tkinter as tk
import threading

app = Bottle()

# Path to the folder containing your score file
SCORES_DIR = r"C:\Users\thisi\Documents\GitHub\CyberHunter-GAME" # Daniel Home Windows
SCORES_DIR = r"C:\Users\COMP5266361\Documents\GitHub\CyberHunter-GAME" # Daniel Work Windows     
SCORES_FILE = "scores.txt"

@app.route('/')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Scores</title>
        </head>
        <body>
            <h1>Scores</h1>
            <p><a href="/scores">Download Scores</a></p>
        </body>
        </html>
    '''

@app.route('/scores')
def serve_scores():
    return static_file(SCORES_FILE, root=SCORES_DIR, download=SCORES_FILE)

def run_server():
    app.run(host="0.0.0.0", port=8080)  # Listen on all interfaces

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    
    root = tk.Tk()
    root.title("Server Status")
    root.configure(bg='black')
    root.geometry("400x200")
    
    label = tk.Label(root, text="Server is running...", fg="white", bg="black", font=("Helvetica", 16))
    label.pack(padx=20, pady=20)
    
    def start_drag(event):
        root.x = event.x
        root.y = event.y

    def on_drag(event):
        x = root.winfo_pointerx() - root.x
        y = root.winfo_pointery() - root.y
        root.geometry(f"+{x}+{y}")

    label.bind("<Button-1>", start_drag)
    label.bind("<B1-Motion>", on_drag)
    
    root.mainloop()
