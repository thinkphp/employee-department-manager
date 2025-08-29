# config_database.py
# Configurația pentru conexiunea la baza de date MySQL

DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'BalabacDB',
    'user': 'snake',
    'password': 'adidas88_AS',
    'port': 3306,
    'charset': 'utf8mb4',
    'autocommit': True
}

# Funcție pentru a obține configurația
def get_database_config():
    return DATABASE_CONFIG.copy()

# Funcție pentru a actualiza configurația (dacă este nevoie)
def update_config(key, value):
    if key in DATABASE_CONFIG:
        DATABASE_CONFIG[key] = value
    else:
        print(f"Cheia '{key}' nu există în configurație!")

# Funcție pentru a verifica configurația
def validate_config():
    required_keys = ['host', 'database', 'user', 'password']
    for key in required_keys:
        if not DATABASE_CONFIG.get(key):
            print(f"Atenție: '{key}' nu este setat în configurație!")
            return False
    return True
