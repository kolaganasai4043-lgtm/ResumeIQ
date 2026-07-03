from flask import Flask, render_template, request, jsonify
import os
from analyzer import analyze_resume

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        if 'resume' not in request.files:
            return jsonify({"error": "No file uploaded"})

        file = request.files['resume']

        if file.filename == '':
            return jsonify({"error": "No file selected"})

        if not file.filename.lower().endswith('.pdf'):
            return jsonify({"error": "Only PDF files are supported. Please upload a .pdf file."})

        job_role = request.form.get('job_role', 'python developer')

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        result = analyze_resume(filepath, job_role)
        print("Result:", result)
        return jsonify(result)

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)