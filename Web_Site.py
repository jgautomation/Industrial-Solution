from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Services Page
@app.route('/services')
def services():
    return render_template('services.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Dummy Data API
@app.route('/data')
def data():
    return jsonify({
        "temperature": random.randint(20, 80),
        "pressure": random.randint(1, 10),
        "production": random.randint(100, 500),
        "status": random.choice(["ON", "OFF"])
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
