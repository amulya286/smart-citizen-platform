from flask import Flask, render_template, request

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')

# LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        return f"Welcome {username}"

    return render_template('login.html')

# FEEDBACK PAGE
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():

    if request.method == 'POST':
        message = request.form['feedback']

        return "Feedback Submitted Successfully"

    return render_template('feedback.html')

# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)