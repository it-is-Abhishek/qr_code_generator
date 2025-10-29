from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS
import qrcode
import io
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css')

@app.route('/index.js')
def js():
    return send_from_directory('.', 'index.js')

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

@app.route("/generate", methods = ["POST"])

def generate_qr():
    data = request.json.get("text")
    if not data:
        return {"error": "no text provided"}, 400

    qr = qrcode.QRCode(box_size = 10, border = 4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="lightyellow")


    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
