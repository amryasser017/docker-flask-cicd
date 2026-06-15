from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    env = os.getenv('APP_ENV')
    return jsonify({
        "message": "Hello from Docker!",
        "developer": "Amr Yasser",
        "status": "running inside a container",
        "environment": env
    })

@app.route('/about')
def about():
    return jsonify({
        "app": "Docker Flask App",
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)