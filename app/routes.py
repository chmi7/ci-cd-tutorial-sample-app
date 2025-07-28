from flask import jsonify
from app import app
from app.models import Menu

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "message": "Welcome to the CI/CD Tutorial App!",
        "available_endpoints": ["/", "/menu", "/status"]
    })

@app.route('/menu')
def menu():
    today = Menu.query.first()
    if today:
        body = { "today_special": today.name }
        status = 200
    else:
        body = { "error": "Sorry, the service is not available today." }
        status = 404
    return jsonify(body), status

@app.route('/status')
def status():
    return jsonify({
        "service": "CI/CD Tutorial App",
        "status": "running",
        "version": "1.0.1"
    })
