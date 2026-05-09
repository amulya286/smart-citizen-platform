from flask import Flask, render_template

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')

# LOGIN PAGE
@app.route('/login')
def login():
    return render_template('login.html')

# FEEDBACK PAGE
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)