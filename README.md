# MySQL Employee GUI

A simple Python GUI application for viewing Employee and Department data from a MySQL database.

## 📋 Description

This application provides a tkinter-based GUI interface to connect and visualize data from two MySQL tables:
- **departament** - company departments information
- **employee** - employee information and their departments

## ✨ Features

- 🔌 **MySQL Connection**: Interface for database connection
- 👥 **View Employees**: Display all records from `employee` table
- 🏢 **View Departments**: Display all records from `departament` table
- 🔄 **Refresh**: Update displayed data
- 📊 **Interactive Table**: Data presented in an easy-to-read table format
- ⚙️ **External Configuration**: Database settings in separate file

## 🗂️ Project Structure

```
mysql-employee-gui/
│
├── main.py                 # Main GUI application
├── config_database.py      # Database configuration
├── database_schema.sql     # CREATE TABLE scripts
├── sample_data.sql         # Test data (INSERT statements)
└── README.md              # This documentation
```

## 🛠️ Installation and Setup

### Prerequisites

- Python 3.6+
- MySQL Server
- `mysql-connector-python` library

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/mysql-employee-gui.git
   cd mysql-employee-gui
   ```

2. **Install dependencies:**
   ```bash
   pip install mysql-connector-python
   ```

3. **Configure database:**
   - Edit the `config_database.py` file
   - Update MySQL credentials:
   ```python
   DATABASE_CONFIG = {
       'host': 'localhost',
       'database': 'your_database_name',
       'user': 'username',
       'password': 'your_password',
       'port': 3306
   }
   ```

4. **Create database structure:**
   ```bash
   mysql -u username -p < database_schema.sql
   ```

5. **Insert test data (optional):**
   ```bash
   mysql -u username -p your_database_name < sample_data.sql
   ```

## 🚀 Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Connect to database:**
   - Check/modify credentials in the interface
   - Click "Conectare" button

3. **View data:**
   - Click "Afișează Employees" to view employees
   - Click "Afișează Departments" to view departments
   - Use "Refresh" to update the data

## 📊 Database Schema

### `departament` Table
| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary key (AUTO_INCREMENT) |
| nume | VARCHAR(50) | Department name (UNIQUE) |
| created_at | TIMESTAMP | Creation timestamp |
| updated_at | TIMESTAMP | Last modification timestamp |

### `employee` Table
| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary key (AUTO_INCREMENT) |
| nume | VARCHAR(100) | Employee full name |
| functie | VARCHAR(50) | Job position/role |
| salariu | DECIMAL(10,2) | Salary (positive values) |
| departament_id | INT | Foreign key to departament |
| created_at | TIMESTAMP | Creation timestamp |
| updated_at | TIMESTAMP | Last modification timestamp |

## 🔧 Technologies Used

- **Python 3** - Main programming language
- **tkinter** - Native Python GUI framework
- **mysql-connector-python** - MySQL driver for Python
- **MySQL** - Database management system

## 📱 Screenshot

```
┌─ Employee & Department Interface ─────────────────────┐
│ ┌─ Database Connection ────────────────────────────┐ │
│ │ Host: [localhost] Database: [company_db]         │ │
│ │ User: [root]      Password: [••••••••]           │ │
│ │              [Connect]                           │ │
│ │ Status: Connected                                │ │
│ └─────────────────────────────────────────────────┘ │
│                                                     │
│ [Show Employees] [Show Departments] [Refresh]       │
│                                                     │
│ ┌─ Data Table ────────────────────────────────────┐ │
│ │ ID │ Name        │ Position     │ Salary  │ Dep││ │
│ │ 1  │ Popescu M.  │ HR Manager   │ 6500.00 │  1 ││ │
│ │ 2  │ Ionescu A.  │ Developer    │ 7800.00 │  2 ││ │
│ │ ... │            │              │         │    ││ │
│ └─────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────┘
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Issues and Troubleshooting

If you encounter problems:

- Verify that MySQL server is running
- Confirm credentials in `config_database.py`
- Ensure tables exist and contain necessary data
- Check that `mysql-connector-python` is installed
- Verify Python version compatibility (3.6+)

## 📝 Sample Data

The repository includes sample data with:
- **5 Departments**: HR, IT, Marketing, Sales, Accounting
- **10 Employees**: Distributed across departments with realistic roles and salaries

## 🔮 Future Enhancements

- [ ] Add CRUD operations (Create, Update, Delete)
- [ ] Employee search and filtering
- [ ] Export data to CSV/Excel
- [ ] Database backup functionality
- [ ] Multi-language support
- [ ] Advanced reporting features
