
import time
import sys

# Fungsi efek ketik
def ketik(teks, delay=0.1 ):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(delay)
    print()  # pindah baris.

# Fungsi untuk menampilkan lirik dengan jeda antar baris & paragraf
def tampilkan_lirik(lirik):
    for baris in lirik:
        if baris.strip() == "":
            time.sleep(0.2)  # jeda antar paragraf
            print()
        else:
            ketik(baris)
            time.sleep(0.2)  # jeda antar baris

# ======================
# LIRIK LAGU (user input)
# ======================

lirik = [
    "Kau bermasalah jiwa aku pun rada gila",
    "Jodoh akal-akalan neraka kita bersama",
    "Kau langganan menangis lakimu muntah-muntah",
    "Begitu terus sampai Iblis tobat dan sedekah",
    "",
    "Terkadang rasa nya leher terbakan hinga pagi",
    "Seperti aku hidup berpasangan dengan api",
    "Berhenti ulangi psikolog dan terapi",
    "Aku isi bensin kita coba lagi",
    "",
    "Tapi sebelumnya sejuta sayang untukmu cinta",
    "Karna aku pun bola panas juga kadang lebih atau sama parahnya",
    "Dan jika bicara tentang masa depan aku pun bingung tak punya tebakan",
    "Lagu cinta untuk akhir dunia lihat kami nyanyikan ini bersama",
    "",
    "Smoga hidup kita trus begini-gini saja",
    "Walau sungai meluap dan kurs tak masuk logika",
    "Smoga kita mencintai apa adanya",
    "Walau katanya skarang ku bisa masuk penjara",
    "",
    "Satu per satu hari per hari",
    "Yang menyakiti benahi lagi",
    "Perihal esok tuk nanti dulu",
    "Perihal cincin kucari waktu",
    "",
    "Persetan kata siapa mau bilang apa tak guna",
    "Mereka hanya tahu namamu mereka takkan jadi diriku",
    "Persetan aturan cinta tak tertulis di atas batu",
    "Apa kau ingin menjadi benar atau ingin menjadi muda",
    "",
    "Smoga hidup kita trus begini-gini saja",
    "Walau sungai meluap dan kurs tak masuk logika",
    "Smoga kita mencintai apa adanya",
    "Walau katanya skarang ku bisa masuk penjara",
    "",
    "Persetan kata siapa mau bilang apa tak guna",
    "Mereka hanya tahu namamu mereka takkan jadi diriku",
    "Persetan aturan cinta tak tertulis di atas batu",
    "Apa kau ingin menjadi benar atau kau ingin menjadi muda",
    "",
    "Lagu cinta untuk akhir dunia",
    "Sekarang bantu aku nyanyikan ini bersama",
    "",
    "Smoga hidup kita trus begini-gini saja",
    "Walau sungai meluap dan kurs tak masuk logika",
    "Smoga kita mencintai apa adanya",
    "Walau katanya skarang ku bisa masuk penjara",
    "",
    "Satu per satu hari per hari",
    "Yang menyakiti benahi lagi",
    "Perihal esok tuk nanti dulu",
    "Perihal cincin kucari waktu"
]

# Jalankan program
print("\n🎵 Menampilkan Lirik Lagu: 'Cincin' - Hindia 🎵\n")
tampilkan_lirik(lirik)
print("\n✅ Lirik selesai ditampilkan.\n")
