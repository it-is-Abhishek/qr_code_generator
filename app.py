from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route("/generate", methods = ["POST"])

def generate_qr():
    data = request.json.get("text")
    if not data:
        return {"error: no text provideed"}, 400
    
    qr = qrcode.QRCode(box_size = 10, border = 4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "purple", back_color = "white")


    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)