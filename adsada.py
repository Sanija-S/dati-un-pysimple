import PySimpleGUI as sg
import sqlite3
#izveidosim datu bāzes savienojumu

conn=sqlite3.connect("pieraksts.db") # parada ka mums bus tads datubazes fails, vienalga kads name
cursor=conn.cursor()



conn.commit()











# aizvert GUI logs un datu bazes savienojums (Parbaudam ka saiet kods)
conn.close()