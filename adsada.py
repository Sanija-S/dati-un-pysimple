import PySimpleGUI as sg
import sqlite3
#izveidosim datu bāzes savienojumu

conn=sqlite3.connect("pieraksts.db") # parada ka mums bus tads datubazes fails, vienalga kads name
cursor=conn.cursor() # objekts kas stradā savienojuma, ko mes izveidojam

#izveidojam tabulu, ja tādas nav!!

cursor.execute(""" CREATE TABLE IF NOT EXISTS lietotāji""") # ar 3 ķepiņām """ vai ''' - sitais ir sq valodā




conn.commit()











# aizvert GUI logs un datu bazes savienojums (Parbaudam ka saiet kods)
conn.close()