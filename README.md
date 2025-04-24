
# SPAS (Smart Portable Analyzer System)

Sistem ini dirancang untuk memantau berbagai parameter kualitas air dan cuaca menggunakan beberapa sensor, serta menyimpan data ke dalam database PostgreSQL.

## 📦 Komponen Utama

### Sensor dan Modul
- **AT500** - membaca parameter pH, TSS, dan NH3-N.
- **MACE** - membaca battery level, kedalaman (depth), dan laju aliran (flow).
- **Spectro COD Sensor (Modbus TCP/IP)** - membaca nilai COD dari sensor melalui protokol Modbus TCP/IP.

### Struktur File
- `main.py` — Program utama yang menggabungkan semua pembacaan sensor dan menyimpan ke database.
- `database.py` — Koneksi dan fungsi penyimpanan data ke PostgreSQL.
- `at500.py`, `mace.py`,  — Modul pembacaan masing-masing sensor.
- `spectro.py` — Modul pembacaan sensor COD via Modbus TCP/IP.

## 🛠️ Cara Kerja

1. Program:
   - Membaca data dari semua sensor.
   - Menampilkan hasil ke terminal.
   - Menyimpan data ke dalam tabel `sensor_datas`.

2. Nilai yang disimpan meliputi:
   - `datetime`, `ph`, `tss`, `nh3n`, `depth`, `flow`, `cod`.

## ⚙️ Database

Pastikan Anda memiliki tabel `sensor_datas` dengan struktur sebagai berikut:

```sql
CREATE TABLE sensor_datas (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMP,
    rain REAL, #optional
    ph REAL,
    tss REAL,
    nh3n REAL,
    depth REAL,
    flow REAL,
    cod REAL
);
```

## 🔌 Konfigurasi

- IP dan port sensor COD dapat disesuaikan di `spectro.py`.
- Parameter koneksi database disesuaikan di `database.py`.

## 🚀 Menjalankan Program

```bash
python main.py
```

## 📋 Catatan

- Sistem akan berhenti dengan `CTRL+C` dan membersihkan proses jika perlu.
- Jika sensor tidak merespons, data akan diabaikan untuk iterasi tersebut.

---

© 2025 PT HAS Environmental
