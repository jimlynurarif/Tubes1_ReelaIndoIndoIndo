# Tubes 1 Strategi Algoritma  
Ini adalah Repository Github Kelompok 53 untuk Tugas Besar 1 IF2211 Strategi Algoritma.  
Pada Tugas Besar ini kami diminta untuk membuat logika bot dalam sebuah permainan yang bernama "Diamonds"  


# Algoritma Greedy  
Program logika bot kami mengimplementasikan kombinasi tiga strategi greedy dalam permainan "Diamonds". Ketiga strategi greedy tersebut adalah:  
- Greedy by Distance, yaitu mengambil diamond yang terdekat dari base.
- Greedy by Weight, yaitu mengambil diamond dengan poin lebih tinggi (diamond merah).
- Greedy by Tackle, melakukan tackle jika ada bot lain yang berpapasan dengan bot kita.

Dengan menggabungkan tiga strategi yang berbeda kami berharap bot yang kami buat bisa beradaptasi dengan berbagai situasi di dalam permainan "Diamonds" selama permainan berlangsung.
 
# Requirement
- Node.js
- Docker desktop
- Yarn
- Game Engine
- Bot Starter Pack
- Python
- IDE (Visual Studio Code)

Game Engine dan Bot Starter Pack dapat diunduh di dari [sini](https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0)

Panduan lengkap instalasi dapat dilihat di [sini](https://docs.google.com/document/d/1L92Axb89yIkom0b24D350Z1QAr8rujvHof7-kXRAp7c/edit)

# Command
## Menjalankan Game Engine
### Konfigurasi awal
- masuk ke direktori project. cd tubes1-IF2110-game-engine-1.1.0
- install dependencies menggunakan Yarn. yarn
- setup default enrvironment variable. ./scripts/copy-env.bat
- setup local database. docker compose up -d database
- jalankan: ./scripts/setup-db-prisma.bat

### Build
- npm run build

### Run 
- npm run start

## Menjalankan Bot
### Konfigurasi awal
- masuk ke direktori project. cd tubes1-IF2110-bot-starter-pack-1.0.1
- install dependencies menggunakan pip. pip install -r requirements.txt

### Run
- jalankan: python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team etimo
- jalankan: ./run-bots.bat

# Identitas
Kelompok 53 Reela Indo Indo Indo
- Jimly Nur Arif (13522123)  
- Yosef Rafael Joshua (13522133)  
- Rayhan Ridhar Rahman (13522160)
