# 📄 PDF → Word Konverter

Jednoduchá webová aplikace pro převod PDF souborů do formátu `.docx`.

---

## 🚀 Rychlý start

### 1. Instalace závislostí
pip install flask pdf2docx

### 2. Spuštění
python app.py

### 3. Otevři v prohlížeči
http://127.0.0.1:5000

---

## 📁 Struktura projektu

projekt/
├── app.py          # Flask backend, přijímá upload a vrací .docx
├── worker.py       # Konverze PDF → DOCX přes pdf2docx
├── uploads/        # Dočasné uložiště souborů (vytvoří se automaticky)
└── templates/
    └── index.html  # Frontend — drag & drop UI

---

## ⚙️ Jak to funguje

1. Uživatel nahraje PDF přes webové rozhraní
2. Flask uloží soubor do složky `uploads/`
3. `worker.py` spustí konverzi pomocí knihovny `pdf2docx`
4. Hotový `.docx` se automaticky stáhne do počítače

---

## 📦 Závislosti

| Balíček | Účel |
|---------|------|
| flask   | Webový server |
| pdf2docx | Konverze PDF na Word |

---

## ⚠️ Poznámky

- Aplikace je určena pro lokální použití
- Před nasazením na server vypni `debug=True` v `app.py`
- Složka `uploads/` není automaticky mazána — soubory se postupně hromadí

---



## 👨‍💻 Autor

Zipoo69....
Python PDF → DOCX converter project 🚀