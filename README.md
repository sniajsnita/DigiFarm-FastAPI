# DigiFarm-FastAPI

# 🌾 Rice Plant Pest & Disease Detection API

API berbasis **FastAPI** dan **YOLOv8** untuk mendeteksi hama dan penyakit tanaman padi. Dibangun sebagai backend inferensi model AI dalam sistem Tugas Akhir yang terintegrasi dengan aplikasi mobile.

---

## 📋 Daftar Kelas Deteksi

| No | Kelas | Keterangan |
|----|-------|-----------|
| 1 | `blast` | Penyakit blas |
| 2 | `blight` | Penyakit hawar daun |
| 3 | `penggerek_batang` | Hama penggerek batang |
| 4 | `wereng_coklat` | Hama wereng coklat |
| 5 | `tungro` | Penyakit tungro |
| 6 | `tikus` | Hama tikus |

---

## 🛠️ Teknologi

- **Python** 3.10+
- **FastAPI** — framework REST API
- **Ultralytics YOLOv8** — model deteksi objek
- **Pillow** — pemrosesan gambar
- **Uvicorn** — ASGI server

---

## 📁 Struktur Proyek

```
.
├── main.py        # Aplikasi FastAPI utama
├── best.pt        # Model YOLOv8 terlatih (tidak di-push ke GitHub)
├── requirements.txt
└── README.md
```

> ⚠️ **Catatan:** File `best.pt` **tidak disertakan** di repository ini karena ukurannya besar. Unduh model secara terpisah ([lihat bagian *Download Model* di bawah]
> https://drive.google.com/file/d/1ciVUFyBLN_HTTk9Y8vx92QtIELx0FWUO/view?usp=sharing

---

## ⚙️ Instalasi & Menjalankan Lokal

### 1. Clone Repository

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 2. Buat Virtual Environment (direkomendasikan)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Letakkan File Model

Salin file `best.pt` ke direktori root proyek (sejajar dengan `main.py`):

```
.
├── main.py
├── best.pt   ← letakkan di sini
└── ...
```

### 5. Jalankan Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000                                                                                        
```

Server akan berjalan di: `http://127.0.0.1:5000`

---

## 📡 Endpoint API

### `GET /`
Cek status server.

**Response:**
```json
{
  "message": "YOLO FastAPI running"
}
```

---

### `POST /predict`
Kirim gambar untuk dideteksi.

**Request:**
- Content-Type: `multipart/form-data`
- Field: `file` (gambar `.jpg`, `.jpeg`, `.png`)

**Contoh menggunakan `curl`:**
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -F "file=@foto_tanaman.jpg"
```

**Response:**
```json
{
  "status": "success",
  "detections": [
    {
      "class": "blast",
      "confidence": 0.8732,
      "bbox": [120.5, 85.3, 340.2, 280.1]
    }
  ]
}
```

| Field | Tipe | Keterangan |
|-------|------|-----------|
| `class` | string | Nama kelas yang terdeteksi |
| `confidence` | float | Tingkat kepercayaan (0–1) |
| `bbox` | array | Koordinat bounding box `[x1, y1, x2, y2]` |

---

## 📦 requirements.txt

Buat file `requirements.txt` dengan isi berikut:

```
fastapi
uvicorn[standard]
ultralytics
pillow
python-multipart
```

Atau generate otomatis dari environment aktif:
```bash
pip freeze > requirements.txt
```

---

## 🚀 Deploy (Opsional)

Untuk deploy ke server/VPS:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Pastikan port 8000 sudah dibuka di firewall/security group server.

---

## 📌 Catatan Pengembangan

- Model di-load **satu kali** saat startup untuk efisiensi memori dan kecepatan inferensi.
- Gambar otomatis di-resize ke maksimal **640px** sebelum inferensi sesuai input optimal YOLOv8.
- CORS diaktifkan untuk semua origin (`*`) — **sesuaikan untuk production** agar lebih aman.

---

## 👩‍💻 Author

**Sonia** — Mahasiswa D3 Sistem Informasi, Telkom University  
Tugas Akhir: *Sistem Deteksi Hama dan Penyakit Tanaman Padi Berbasis YOLOv8 dengan Aplikasi Mobile*
