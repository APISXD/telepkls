import locale
from datetime import datetime
from telegram import ParseMode

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define conversation states
CHOOSING, AREA_CHOICE, CIRCLE_RADIUS, TRIANGLE_BASE, TRIANGLE_HEIGHT, SQUARE_LENGTH, SQUARE_WIDTH, PARALLELOGRAM_BASE, PARALLELOGRAM_HEIGHT, SALARY_NAME, SALARY_AMOUNT, SALARY_ATTENDANCE = range(12)

# Start command
def start(update, context):
    update.message.reply_text("Halo! Saya adalah bot kalkulator. Silakan pilih opsi:\n"
                              "1. Menghitung Luas\n"
                              "2. Menghitung gaji bulanan")
    return CHOOSING

# Choose option
def choose_option(update, context):
    text = update.message.text
    if text == '1':
        update.message.reply_text("Pilih jenis luas yang ingin Anda hitung:\n"
                                  "1. Lingkaran\n"
                                  "2. Segitiga\n"
                                  "3. Persegi\n"
                                  "4. Jajargenjang")
        return AREA_CHOICE
    elif text == '2':
        update.message.reply_text("Masukkan informasi gaji bulanan:\n"
                                  "1. Nama\n"
                                  "2. Gaji\n"
                                  "3. Jumlah Kehadiran")
        return SALARY_NAME
    else:
        update.message.reply_text("Input tidak valid. Silakan pilih opsi 1 atau 2.")
        return CHOOSING

# Handle area calculation
def handle_area_calculation(update, context):
    option = int(update.message.text)

    if option == 1:
        update.message.reply_text("Masukkan jari-jari lingkaran:")
        return CIRCLE_RADIUS
    elif option == 2:
        update.message.reply_text("Masukkan alas segitiga:")
        return TRIANGLE_BASE
    elif option == 3:
        update.message.reply_text("Masukkan panjang persegi:")
        return SQUARE_LENGTH
    elif option == 4:
        update.message.reply_text("Masukkan alas jajargenjang:")
        return PARALLELOGRAM_BASE
    else:
        update.message.reply_text("Pilihan tidak valid. Silakan pilih angka 1-4.")
        return AREA_CHOICE

# Handle circle radius input
def handle_circle_radius(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return choose_option(update, context)
    
    context.user_data['radius'] = float(text)
    luas = 3.14 * context.user_data['radius'] ** 2
    update.message.reply_text(f"Luas lingkaran adalah: {luas}")
    return CHOOSING

# Handle triangle base input
def handle_triangle_base(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return choose_option(update, context)
    
    context.user_data['base'] = float(text)
    update.message.reply_text("Masukkan tinggi segitiga:")
    return TRIANGLE_HEIGHT

# Handle triangle height input
def handle_triangle_height(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return handle_triangle_base(update, context)
    
    height = float(text)
    luas = 0.5 * context.user_data['base'] * height
    update.message.reply_text(f"Luas segitiga adalah: {luas}")
    return CHOOSING

# Handle square length input
def handle_square_length(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return choose_option(update, context)
    
    context.user_data['length'] = float(text)
    update.message.reply_text("Masukkan lebar persegi:")
    return SQUARE_WIDTH

# Handle square width input
def handle_square_width(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return handle_square_length(update, context)
    
    width = float(text)
    luas = context.user_data['length'] * width
    update.message.reply_text(f"Luas persegi adalah: {luas}")
    return CHOOSING

# Handle parallelogram base input
def handle_parallelogram_base(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return choose_option(update, context)
    
    context.user_data['base'] = float(text)
    update.message.reply_text("Masukkan tinggi jajargenjang:")
    return PARALLELOGRAM_HEIGHT

# Handle parallelogram height input
def handle_parallelogram_height(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return handle_parallelogram_base(update, context)
    
    height = float(text)
    luas = context.user_data['base'] * height
    update.message.reply_text(f"Luas jajargenjang adalah: {luas}")
    return CHOOSING

# Handle salary name input
def handle_salary_name(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return choose_option(update, context)
    
    context.user_data['name'] = text
    update.message.reply_text("Masukkan gaji (tanpa koma/titik):")
    return SALARY_AMOUNT

# Handle salary amount input
def handle_salary_amount(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return handle_salary_name(update, context)
    
    context.user_data['salary'] = float(text)
    update.message.reply_text("Masukkan jumlah kehadiran:")
    return SALARY_ATTENDANCE

# Handle salary attendance input
def handle_salary_attendance(update, context):
    text = update.message.text
    if text.lower() == 'kembali':
        return handle_salary_amount(update, context)
    
    attendance = int(text)
    total_salary = context.user_data['salary'] * attendance
    formatted_salary = locale.format_string("%.2f", total_salary, grouping=True)
    update.message.reply_text(f"Total gaji bulanan untuk {context.user_data['name']} adalah: {formatted_salary}")
    return CHOOSING

import locale

# Set locale
locale.setlocale(locale.LC_ALL, 'id_ID')  # Sesuaikan dengan kode bahasa dan wilayah Anda

# Handle /count command
def count(update, context):
    update.message.reply_text("Menghitung jumlah kata dalam pesan...")
    words_count = len(context.args)
    update.message.reply_text(f"Jumlah kata dalam pesan adalah: {words_count}")

# Handle /sekejul command
def sekejul(update, context):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    update.message.reply_text(f"Waktu sekarang adalah: {current_time} dan Kereta disini https://commuterline.id/perjalanan-krl/jadwal-kereta")

# Cancel function
def cancel(update, context):
    update.message.reply_text("Operasi dibatalkan.")
    return ConversationHandler.END

# Define the /skul command handler
def skul(update, context):
    # Path to your image file
    image_path = "jadwalskul.jpg"  # Ganti dengan path file gambar Anda

    # Caption text
    caption = "Jadwal Sekolah 11 DKV D."

    # Kirim gambar beserta keterangan teks
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image_path, 'rb'), caption=caption, parse_mode=ParseMode.HTML)

# Main function
def main():
    updater = Updater("7064293514:AAETZculIm7nX_dHaGIaFFLaamUj-8qQDlY", use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(Filters.regex(r'^[12]$'), choose_option)],
            AREA_CHOICE: [MessageHandler(Filters.regex(r'^[1-4]$'), handle_area_calculation)],
            CIRCLE_RADIUS: [MessageHandler(Filters.text & ~Filters.command, handle_circle_radius)],
            TRIANGLE_BASE: [MessageHandler(Filters.text & ~Filters.command, handle_triangle_base)],
            TRIANGLE_HEIGHT: [MessageHandler(Filters.text & ~Filters.command, handle_triangle_height)],
            SQUARE_LENGTH: [MessageHandler(Filters.text & ~Filters.command, handle_square_length)],
            SQUARE_WIDTH: [MessageHandler(Filters.text & ~Filters.command, handle_square_width)],
            PARALLELOGRAM_BASE: [MessageHandler(Filters.text & ~Filters.command, handle_parallelogram_base)],
            PARALLELOGRAM_HEIGHT: [MessageHandler(Filters.text & ~Filters.command, handle_parallelogram_height)],
            SALARY_NAME: [MessageHandler(Filters.text & ~Filters.command, handle_salary_name)],
            SALARY_AMOUNT: [MessageHandler(Filters.text & ~Filters.command, handle_salary_amount)],
            SALARY_ATTENDANCE: [MessageHandler(Filters.text & ~Filters.command, handle_salary_attendance)]
        },
        fallbacks=[MessageHandler(Filters.regex(r'^cancel$'), cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("count", count))
    dp.add_handler(CommandHandler("sekejul", sekejul))
    dp.add_handler(CommandHandler("skul", skul))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
