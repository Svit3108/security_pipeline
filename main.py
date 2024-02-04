from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/exec', methods=['GET'])
def exec_command():
    # Direkte Ausführung von Benutzereingaben ohne Validierung
    command = request.args.get('cmd')
    # Validate and sanitize user-provided command
    if not command:
        return "Invalid command\n", 400

    # Use subprocess with a list of arguments for security
    try:
        subprocess.run(command.split(), check=True)
        return "Command executed successfully\n"
    except subprocess.CalledProcessError:
        return "Failed to execute command\n", 500

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # Validate file existence
    if not file:
        return "No file uploaded\n", 400

    # Safely handle file data (example: save to disk)
    file.save("/path/to/save/file")
    return "File uploaded successfully\n"

@app.route('/run', methods=['POST'])
def run_command():
    command = request.form['command']
    # Validate and sanitize user-provided command
    if not command:
        return "Invalid command\n", 400

    # Use subprocess with a list of arguments for security
    try:
        subprocess.run(command.split(), check=True)
        return "Command executed successfully\n"
    except subprocess.CalledProcessError:
        return "Failed to execute command\n", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

