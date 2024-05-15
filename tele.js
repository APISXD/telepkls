const { Telegraf } = require('telegraf');

// Inisialisasi bot Telegram dengan token Anda
const bot = new Telegraf('YOUR_BOT_TOKEN');

// Router untuk mengarahkan pesan ke fungsi yang benar
const router = async (ctx, next) => {
    const message = ctx.update.message;
    const text = message.text;

    if (text === '/start') {
        start(ctx);
    } else if (text === '1') {
        calculateArea(ctx);
    } else if (text === '2') {
        calculateSalary(ctx);
    } else {
        ctx.reply('Input tidak valid. Silakan pilih opsi 1 atau 2.');
    }
};

// Fungsi untuk memulai percakapan
const start = (ctx) => {
    ctx.reply("Halo! Saya adalah bot kalkulator. Silakan pilih opsi:\n"
              "1. Menghitung Luas\n"
              "2. Menghitung gaji bulanan");
};

// Fungsi untuk menghitung luas
const calculateArea = async (ctx) => {
    await ctx.reply("Pilih jenis luas yang ingin Anda hitung:\n"
                    "1. Lingkaran\n"
                    "2. Segitiga\n"
                    "3. Persegi\n"
                    "4. Jajargenjang");

    // Menangkap input dari pengguna
    bot.on('text', async (ctx) => {
        const message = ctx.update.message;
        const text = message.text;

        // Handle input pengguna untuk setiap jenis luas
        if (text === '1') {
            await ctx.reply("Masukkan jari-jari lingkaran:");
            bot.on('text', async (ctx) => {
                const r = parseFloat(ctx.update.message.text);
                const luas = 3.14 * r * r;
                await ctx.reply(`Luas lingkaran adalah: ${luas}`);
                calculateArea(ctx); // Kembali ke menu calculateArea
            });
        } else if (text === '2') {
            await ctx.reply("Masukkan alas segitiga:");
            bot.on('text', async (ctx) => {
                const a = parseFloat(ctx.update.message.text);
                await ctx.reply("Masukkan tinggi segitiga:");
                bot.on('text', async (ctx) => {
                    const t = parseFloat(ctx.update.message.text);
                    const luas = (a * t) / 2;
                    await ctx.reply(`Luas segitiga adalah: ${luas}`);
                    calculateArea(ctx); // Kembali ke menu calculateArea
                });
            });
        } else if (text === '3') {
            await ctx.reply("Masukkan panjang persegi:");
            bot.on('text', async (ctx) => {
                const p = parseFloat(ctx.update.message.text);
                await ctx.reply("Masukkan lebar persegi:");
                bot.on('text', async (ctx) => {
                    const l = parseFloat(ctx.update.message.text);
                    const luas = p * l;
                    await ctx.reply(`Luas persegi adalah: ${luas}`);
                    calculateArea(ctx); // Kembali ke menu calculateArea
                });
            });
        } else if (text === '4') {
            await ctx.reply("Masukkan alas jajargenjang:");
            bot.on('text', async (ctx) => {
                const a = parseFloat(ctx.update.message.text);
                await ctx.reply("Masukkan tinggi jajargenjang:");
                bot.on('text', async (ctx) => {
                    const t = parseFloat(ctx.update.message.text);
                    const luas = a * t;
                    await ctx.reply(`Luas jajargenjang adalah: ${luas}`);
                    calculateArea(ctx); // Kembali ke menu calculateArea
                });
            });
        } else {
            await ctx.reply('Input tidak valid. Silakan pilih angka 1-4.');
            calculateArea(ctx); // Kembali ke menu calculateArea
        }
    });
};

// Fungsi untuk menghitung gaji bulanan
const calculateSalary = async (ctx) => {
    await ctx.reply("Masukkan informasi gaji bulanan:\n"
                    "1. Nama\n"
                    "2. Gaji\n"
                    "3. Jumlah Kehadiran");

    // Menangkap input dari pengguna
    bot.on('text', async (ctx) => {
        const message = ctx.update.message;
        const text = message.text;

        // Handle input pengguna untuk menghitung gaji bulanan
        if (text === '1') {
            await ctx.reply("Masukkan nama:");
            bot.on('text', async (ctx) => {
                const nama = ctx.update.message.text;
                await ctx.reply("Masukkan gaji:");
                bot.on('text', async (ctx) => {
                    const gaji = parseFloat(ctx.update.message.text);
                    await ctx.reply("Masukkan jumlah kehadiran:");
                    bot.on('text', async (ctx) => {
                        const kehadiran = parseFloat(ctx.update.message.text);
                        const totalGaji = gaji * kehadiran;
                        await ctx.reply(`Total gaji bulanan untuk ${nama} adalah: ${totalGaji}`);
                    });
                });
            });
        } else {
            await ctx.reply('Input tidak valid. Silakan masukkan informasi dengan benar.');
            calculateSalary(ctx); // Kembali ke menu calculateSalary
        }
    });
};

// Jalankan router pada bot
bot.on('text', router);

// Mulai bot
bot.launch();
