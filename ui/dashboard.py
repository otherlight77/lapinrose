import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('LapinRose v0.3')
root.geometry('1000x700')

title = tk.Label(root, text='LapinRose v0.3', font=('Arial', 22, 'bold'))
title.pack(pady=10)

tabs = ttk.Notebook(root)
tabs.pack(fill='both', expand=True)

dashboard_tab = ttk.Frame(tabs)
ftp_tab = ttk.Frame(tabs)
sql_tab = ttk.Frame(tabs)
github_tab = ttk.Frame(tabs)
mining_tab = ttk.Frame(tabs)
crypto_tab = ttk.Frame(tabs)
logs_tab = ttk.Frame(tabs)

tabs.add(dashboard_tab, text='Dashboard')
tabs.add(ftp_tab, text='FTP')
tabs.add(sql_tab, text='SQL')
tabs.add(github_tab, text='GitHub')
tabs.add(mining_tab, text='Mining')
tabs.add(crypto_tab, text='Crypto')
tabs.add(logs_tab, text='Logs')

tk.Label(dashboard_tab, text='Bienvenue dans LapinRose', font=('Arial', 16)).pack(pady=20)

logbox = tk.Text(logs_tab)
logbox.pack(fill='both', expand=True)

root.mainloop()
