import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
from config_database import get_database_config

class DatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfața Employee & Department")
        self.root.geometry("800x600")
        
        # Variabile pentru conexiunea la baza de date
        self.connection = None
        self.db_config = get_database_config()
        
        # Crearea interfței
        self.create_widgets()
        
    def create_widgets(self):
        # Frame pentru conexiunea la baza de date
        connection_frame = ttk.LabelFrame(self.root, text="Conexiune Baza de Date", padding="10")
        connection_frame.pack(fill="x", padx=10, pady=5)
        
        # Câmpuri pentru conexiune
        ttk.Label(connection_frame, text="Host:").grid(row=0, column=0, sticky="w", padx=5)
        self.host_entry = ttk.Entry(connection_frame, width=15)
        self.host_entry.insert(0, self.db_config['host'])
        self.host_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(connection_frame, text="Database:").grid(row=0, column=2, sticky="w", padx=5)
        self.database_entry = ttk.Entry(connection_frame, width=15)
        self.database_entry.insert(0, self.db_config['database'])
        self.database_entry.grid(row=0, column=3, padx=5)
        
        ttk.Label(connection_frame, text="User:").grid(row=1, column=0, sticky="w", padx=5)
        self.user_entry = ttk.Entry(connection_frame, width=15)
        self.user_entry.insert(0, self.db_config['user'])
        self.user_entry.grid(row=1, column=1, padx=5)
        
        ttk.Label(connection_frame, text="Password:").grid(row=1, column=2, sticky="w", padx=5)
        self.password_entry = ttk.Entry(connection_frame, show="*", width=15)
        self.password_entry.insert(0, self.db_config['password'])
        self.password_entry.grid(row=1, column=3, padx=5)
        
        # Buton pentru conectare
        self.connect_btn = ttk.Button(connection_frame, text="Conectare", command=self.connect_database)
        self.connect_btn.grid(row=2, column=0, columnspan=4, pady=10)
        
        # Status label
        self.status_label = ttk.Label(connection_frame, text="Status: Neconectat", foreground="red")
        self.status_label.grid(row=3, column=0, columnspan=4)
        
        # Frame pentru butoane
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(fill="x", padx=10, pady=10)
        
        # Butoane pentru query-uri
        self.employee_btn = ttk.Button(buttons_frame, text="Afișează Employees", 
                                     command=self.show_employees, state="disabled")
        self.employee_btn.pack(side="left", padx=10)
        
        self.department_btn = ttk.Button(buttons_frame, text="Afișează Departments", 
                                       command=self.show_departments, state="disabled")
        self.department_btn.pack(side="left", padx=10)
        
        # Buton pentru refresh
        self.refresh_btn = ttk.Button(buttons_frame, text="Refresh", 
                                    command=self.refresh_current_view, state="disabled")
        self.refresh_btn.pack(side="left", padx=10)
        
        # Frame pentru treeview
        tree_frame = ttk.Frame(self.root)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Treeview pentru afișarea datelor
        self.tree = ttk.Treeview(tree_frame)
        self.tree.pack(side="left", fill="both", expand=True)
        
        # Scrollbar pentru treeview
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Variabilă pentru a ține minte ce tabel este afișat
        self.current_table = None
        
    def connect_database(self):
        try:
            # Închiderea conexiunii existente dacă există
            if self.connection and self.connection.is_connected():
                self.connection.close()
            
            # Crearea unei noi conexiuni
            self.connection = mysql.connector.connect(
                host=self.host_entry.get(),
                database=self.database_entry.get(),
                user=self.user_entry.get(),
                password=self.password_entry.get()
            )
            
            if self.connection.is_connected():
                self.status_label.config(text="Status: Conectat", foreground="green")
                self.employee_btn.config(state="normal")
                self.department_btn.config(state="normal")
                self.refresh_btn.config(state="normal")
                messagebox.showinfo("Succes", "Conectat cu succes la baza de date!")
                
        except Error as e:
            self.status_label.config(text="Status: Eroare conexiune", foreground="red")
            messagebox.showerror("Eroare", f"Eroare la conectarea la baza de date: {e}")
            
    def show_employees(self):
        if not self.connection or not self.connection.is_connected():
            messagebox.showerror("Eroare", "Nu există conexiune la baza de date!")
            return
            
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM employee")
            records = cursor.fetchall()
            
            # Obținem numele coloanelor
            column_names = [desc[0] for desc in cursor.description]
            
            # Configurarea treeview-ului
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = column_names
            self.tree["show"] = "headings"
            
            # Configurarea header-elor
            for col in column_names:
                self.tree.heading(col, text=col.title())
                self.tree.column(col, width=100, anchor="center")
            
            # Adăugarea datelor
            for record in records:
                self.tree.insert("", "end", values=record)
                
            self.current_table = "employee"
            cursor.close()
            
            messagebox.showinfo("Info", f"Afișate {len(records)} înregistrări din tabelul Employee")
            
        except Error as e:
            messagebox.showerror("Eroare", f"Eroare la executarea query-ului: {e}")
            
    def show_departments(self):
        if not self.connection or not self.connection.is_connected():
            messagebox.showerror("Eroare", "Nu există conexiune la baza de date!")
            return
            
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM departament")
            records = cursor.fetchall()
            
            # Obținem numele coloanelor
            column_names = [desc[0] for desc in cursor.description]
            
            # Configurarea treeview-ului
            self.tree.delete(*self.tree.get_children())
            self.tree["columns"] = column_names
            self.tree["show"] = "headings"
            
            # Configurarea header-elor
            for col in column_names:
                self.tree.heading(col, text=col.title())
                self.tree.column(col, width=150, anchor="center")
            
            # Adăugarea datelor
            for record in records:
                self.tree.insert("", "end", values=record)
                
            self.current_table = "departament"
            cursor.close()
            
            messagebox.showinfo("Info", f"Afișate {len(records)} înregistrări din tabelul Department")
            
        except Error as e:
            messagebox.showerror("Eroare", f"Eroare la executarea query-ului: {e}")
            
    def refresh_current_view(self):
        if self.current_table == "employee":
            self.show_employees()
        elif self.current_table == "departament":
            self.show_departments()
        else:
            messagebox.showinfo("Info", "Nu există un tabel selectat pentru refresh!")
            
    def on_closing(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = DatabaseGUI(root)
    
    # Gestionarea închiderii aplicației
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    root.mainloop()

if __name__ == "__main__":
    main()
