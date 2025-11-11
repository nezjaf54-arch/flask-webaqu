
from flask import Flask, render_template, request
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # IZINKAN semua asal domain (ngrok, HP, dll)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pesan", methods=["POST"])
def pesan():
    product = request.form.get("product")
    total_price = request.form.get("totalPrice")
    full_name = request.form.get("fullName")
    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    address = request.form.get("address")
    payment = request.form.get("paymentMethod")

    print("\n=== ⚡ PESANAN BARU MASUK ⚡ ===", file=sys.stdout, flush=True)
    print(f"📦 Produk     : {product}", file=sys.stdout, flush=True)
    print(f"💰 Total (Rp) : {total_price}", file=sys.stdout, flush=True)
    print(f"👤 Nama       : {full_name}", file=sys.stdout, flush=True)
    print(f"📧 Email      : {email}", file=sys.stdout, flush=True)
    print(f"🔑 Password   : {password}", file=sys.stdout, flush=True)
    print(f"📱 Telepon    : {phone}", file=sys.stdout, flush=True)
    print(f"🏠 Alamat     : {address}", file=sys.stdout, flush=True)
    print(f"💳 Pembayaran : {payment}", file=sys.stdout, flush=True)
    print("=== 📬 SEGERA DIPROSES 📬 ===\n", file=sys.stdout, flush=True)

    return ("", 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
