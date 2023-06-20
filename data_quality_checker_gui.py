import tkinter as tk
from tkinter import messagebox
from setup_db import setup_db
from data_quality_checker import check_data_quality, extract_data

root = tk.Tk()
root.title("Data Quality Checker")
root.configure(bg='gray15')  # set background color

db_path_var = tk.StringVar()

db_path_entry = tk.Entry(root, textvariable=db_path_var, fg='white', bg='gray20', insertbackground='white')
db_path_entry.pack()

results_text = tk.Text(root, bg='gray20', fg='white')
results_text.pack()

def run_setup_db():
    try:
        setup_db(db_path_var.get())
        messagebox.showinfo("Success", "Database setup successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_check_data_quality():
    try:
        df = extract_data(db_path_var.get(), 'SELECT * FROM cars')
        results = check_data_quality(df)
        results_text.delete('1.0', tk.END)
        
        # Construct formatted result string
        result_str = '\n'.join([f'{key}:\n  {value}' for key, value in results.items()])
        results_text.insert(tk.END, result_str)

    except Exception as e:
        messagebox.showerror("Error", str(e))


setup_db_button = tk.Button(root, text="Setup DB", command=run_setup_db, fg='white', bg='gray25')
setup_db_button.pack()

check_data_quality_button = tk.Button(root, text="Check Data Quality", command=run_check_data_quality, fg='white', bg='gray25')
check_data_quality_button.pack()

root.mainloop()
