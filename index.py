# Mengimpor modul pyautogui, time, dan easygui
import pyautogui
import time
import easygui

# Mendefinisikan kelas AutoGuiBot
class AutoGuiBot:
    # Inisialisasi objek AutoGuiBot
    def __init__(self, messages=None):
        # Memeriksa apakah pesan telah disediakan
        if messages:
            self.messages = messages
        else:
            # Jika tidak, pesan default adalah "Test pyautogui"
            self.messages = ["Test pyautogui"]

    # Metode untuk menjalankan bot
    # Parameter:
    # delay: Waktu jeda antara pengiriman pesan dalam detik, default adalah 0.5 detik
    def run(self, delay=0.5):
        # Loop melalui setiap pesan yang disediakan
        for message in self.messages:
            # Mendapatkan posisi kursor saat ini
            current_position = pyautogui.position()
            # Mengetik pesan ke dalam GUI
            pyautogui.typewrite(message)
            # Menunggu selama delay detik
            time.sleep(delay)
            # Menekan tombol enter
            pyautogui.press("enter")
            # Mengembalikan kursor ke posisi awal
            pyautogui.moveTo(current_position)

# Fungsi untuk mendapatkan pesan dari file teks
def get_messages_from_file():
    # Membuka dialog untuk memilih file
    file_path = easygui.fileopenbox(title="Pilih file pesan", filetypes=["*.txt"])
    # Jika file dipilih
    if file_path:
        # Membaca isi file dan mengembalikan setiap baris sebagai pesan
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    return []

# Fungsi utama
def main():
    # Menampilkan dialog untuk memilih opsi
    choice = easygui.buttonbox("Pilih opsi:", choices=["File", "Statis"])
    # Jika opsi "File" dipilih
    if choice == "File":
        # Mendapatkan pesan dari file
        messages = get_messages_from_file()
        # Jika pesan ditemukan dalam file
        if messages:
            # Membuat instance AutoGuiBot dengan pesan dari file dan menjalankan bot
            bot = AutoGuiBot(messages)
            bot.run()
        else:
            # Menampilkan pesan kesalahan jika tidak ada pesan dalam file yang dipilih
            easygui.msgbox("Tidak ada pesan yang ditemukan dalam file yang dipilih.")
    # Jika opsi "Statis" dipilih
    elif choice == "Statis":
        # Meminta pengguna untuk memasukkan pesan dan jumlah pesan yang ingin dikirim
        message = easygui.enterbox(msg="Masukkan pesan yang ingin dikirim:", title="Pesan Statis")
        num_messages = easygui.integerbox(msg="Masukkan jumlah pesan yang ingin dikirim:", title="Jumlah Pesan", default=1)
        # Membuat list pesan yang berisi pesan yang sama sebanyak jumlah pesan yang diminta
        messages = [message] * num_messages
        # Membuat instance AutoGuiBot dengan pesan statis dan menjalankan bot
        bot = AutoGuiBot(messages)
        bot.run()
    else:
        # Menampilkan pesan kesalahan jika opsi tidak valid
        easygui.msgbox("Opsi tidak valid.")

# Menjalankan fungsi main jika script dijalankan langsung (bukan diimpor sebagai modul)
if __name__ == "__main__":
    main()
