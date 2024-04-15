import PySimpleGUI as sg
import sqlite3
#izveidosim datu bāzes savienojumu

conn=sqlite3.connect("pieraksts.db") # parada ka mums bus tads datubazes fails, vienalga kads name-- paradas kreisaja sturiti pie failiem :)
cursor=conn.cursor() # objekts kas stradā savienojuma, ko mes izveidojam

#izveidojam tabulu, ja tādas nav!!

cursor.execute(""" CREATE TABLE IF NOT EXISTS lietotāji(
               ID INTEGER PRIMARY KEY ,
               vards TEXT,
               uzvards TEXT,
               epasts TEXT
               
)""") # ar 3 ķepiņām """ vai ''' - sitais ir sq valodā




conn.commit()

# izveidojam loga izkārtojumu- lai var redzēt GUI logā

layout=[
   [sg.T("Vards"), sg.InputText(key="Vards")], 
   [sg.T("uzVards"), sg.InputText(key="uzVards")], 
   [sg.T("epasts"), sg.InputText(key="epasts")], 
   [sg.Button("Iesniegt"), sg.Button("Iziet")]


]

logs=sg.Window("Datu bāze", layout, resizable=True)


while True: 
    event,values=logs.read()
    if event ==sg.WIN_CLOSED or event=="Iziet":
        break
""" or...
while True: 
    event,values=logs.read()
    if event is None or event=="Iziet":
        break
"""





# aizvert GUI logs un datu bazes savienojums (Parbaudam ka saiet kods)
conn.close()
