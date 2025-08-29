# MySQL Employee GUI

O interfață grafică simplă în Python pentru vizualizarea datelor din tabelele Employee și Department dintr-o bază de date MySQL.

## 📋 Descriere

Această aplicație oferă o interfață GUI construită cu tkinter pentru a conecta și vizualiza date din două tabele MySQL:
- **departament** - informații despre departamentele companiei
- **employee** - informații despre angajați și departamentele lor

## ✨ Funcționalități

- 🔌 **Conexiune MySQL**: Interface pentru conectarea la baza de date
- 👥 **Vizualizare Employees**: Afișează toate înregistrările din tabelul `employee`
- 🏢 **Vizualizare Departments**: Afișează toate înregistrările din tabelul `departament`
- 🔄 **Refresh**: Actualizează datele afișate
- 📊 **Tabel interactiv**: Date prezentate într-un format tabel ușor de citit
- ⚙️ **Configurare externă**: Setări de bază de date în fișier separat

## 🗂️ Structura Proiectului

```
mysql-employee-gui/
│
├── main.py                 # Aplicația principală GUI
├── config_database.py      # Configurații pentru baza de date
├── database_schema.sql     # Script-uri CREATE TABLE
├── sample_data.sql         # Date de test (INSERT statements)
└── README.md              # Această documentație
```

## 🛠️ Instalare și Configurare

### Prerequisite

- Python 3.6+
- MySQL Server
- Biblioteca `mysql-connector-python`

### Pasii de instalare

1. **Clonează repository-ul:**
   ```bash
   git clone https://github.com/username/mysql-employee-gui.git
   cd mysql-employee-gui
   ```

2. **Instalează dependențele:**
   ```bash
   pip install mysql-connector-python
   ```

3. **Configurează baza de date:**
   - Editează fișierul `config_database.py`
   - Actualizează credențialele MySQL:
   ```python
   DATABASE_CONFIG = {
       'host': 'localhost',
       'database': 'nume_baza_ta',
       'user': 'username',
       'password': 'parola_ta',
       'port': 3306
   }
   ```

4. **Creează structura bazei de date:**
   ```bash
   mysql -u username -p < database_schema.sql
   ```

5. **Inserează datele de test (opțional):**
   ```bash
   mysql -u username -p nume_baza_ta < sample_data.sql
   ```

## 🚀 Utilizare

1. **Rulează aplicația:**
   ```bash
   python main.py
   ```

2. **Conectează-te la baza de date:**
   - Verifică/modifică credențialele în interfață
   - Apasă butonul "Conectare"

3. **Vizualizează datele:**
   - Apasă "Afișează Employees" pentru a vedea angajații
   - Apasă "Afișează Departments" pentru a vedea departamentele
   - Folosește "Refresh" pentru a actualiza datele

## 📊 Schema Bazei de Date

### Tabelul `departament`
| Coloană | Tip | Descriere |
|---------|-----|-----------|
| id | INT | Cheie primară (AUTO_INCREMENT) |
| nume | VARCHAR(50) | Numele departamentului (UNIQUE) |
| created_at | TIMESTAMP | Data creării |
| updated_at | TIMESTAMP | Data ultimei modificări |

### Tabelul `employee`
| Coloană | Tip | Descriere |
|---------|-----|-----------|
| id | INT | Cheie primară (AUTO_INCREMENT) |
| nume | VARCHAR(100) | Numele complet al angajatului |
| functie | VARCHAR(50) | Funcția/poziția |
| salariu | DECIMAL(10,2) | Salariul (pozitiv) |
| departament_id | INT | Foreign key către departament |
| created_at | TIMESTAMP | Data creării |
| updated_at | TIMESTAMP | Data ultimei modificări |

## 🔧 Tehnologii Folosite

- **Python 3** - Limbajul de programare principal
- **tkinter** - Framework GUI nativ Python
- **mysql-connector-python** - Driver pentru conectarea la MySQL
- **MySQL** - Sistem de management al bazei de date

## 📱 Screenshot

```
┌─ Interfața Employee & Department ─────────────────────┐
│ ┌─ Conexiune Baza de Date ─────────────────────────┐ │
│ │ Host: [localhost] Database: [company_db]         │ │
│ │ User: [root]      Password: [••••••••]           │ │
│ │              [Conectare]                         │ │
│ │ Status: Conectat                                 │ │
│ └─────────────────────────────────────────────────┘ │
│                                                     │
│ [Afișează Employees] [Afișează Departments] [Refresh] │
│                                                     │
│ ┌─ Tabel Date ────────────────────────────────────┐ │
│ │ ID │ Nume        │ Funcție      │ Salariu │ Dep││ │
│ │ 1  │ Popescu M.  │ HR Manager   │ 6500.00 │  1 ││ │
│ │ 2  │ Ionescu A.  │ Developer    │ 7800.00 │  2 ││ │
│ │ ... │            │              │         │    ││ │
│ └─────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────┘
```

