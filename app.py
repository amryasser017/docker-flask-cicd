from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Docker!",
        "developer": "Amr Yasser",
        "status": "running inside a container"
    })

@app.route('/about')
def about():
    return jsonify({
        "app": "Docker Flask App",
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)