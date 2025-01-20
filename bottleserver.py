from bottle import Bottle, static_file, template

app = Bottle()

# Path to the folder containing your score file
SCORES_DIR = r"C:\Users\thisi\Documents\cyberhunter"
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
