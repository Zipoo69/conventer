# conventer
# 📄 PDF → DOCX Converter (Web App)

Jednoduchá webová aplikace v Pythonu pro převod PDF souborů do Word dokumentů (.docx).

## 🚀 Funkce
- Nahrání PDF souboru přes webového rozhraní
- Automatická konverze do DOCX
- Stažení výsledného Word souboru
- Jednoduché a moderní UI

## 🛠 Použité technologie
- Python
- Flask
- pdf2docx
- PyMuPDF

## 📁 Struktura projektu

```text
PDF-converter/
├─ app.py
├─ worker.py
├─ templates/
│  └─ index.html
├─ uploads/
└─ README.md
```

## 📦 Instalace

Naklonování repozitáře:

```bash
git clone https://github.com/Zipoo69/conventer.git
cd conventer
```

Vytvoření virtuálního prostředí:

```bash
python -m venv venv
venv\Scripts\activate
```

Instalace závislostí:

```bash
pip install flask pdf2docx pymupdf
```

## ▶ Spuštění

```bash
python app.py
```

Otevři v prohlížeči:

```text
http://127.0.0.1:5000/
```

## ⚙ Jak funguje
1. Nahraješ PDF
2. Flask soubor uloží
3. `worker.py` provede konverzi
4. DOCX se automaticky stáhne

## ⚠️ Poznámky
- Nejlépe funguje pro textová PDF
- U složitějšího layoutu může dojít k drobnému rozhození formátování
- `uploads/` slouží jako dočasná složka

## 👨‍💻 Autor
Python PDF → DOCX converter project 🚀