import PySimpleGUI as sg
import sqlite3
#izveidosim datu bāzes savienojumu

conn=sqlite3.connect("pieraksts.db") # parada ka mums bus tads datubazes fails, vienalga kads name-- paradas kreisaja sturiti pie failiem :)
cursor=conn.cursor() # objekts kas stradā savienojuma, ko mes izveidojam

#izveidojam tabulu, ja tādas nav!!

cursor.execute(""" CREATE TABLE IF NOT EXISTS lietotaji(
               ID INTEGER PRIMARY KEY ,
               vards TEXT,
               uzvards TEXT,
               epasts TEXT
               
)""") # ar 3 ķepiņām """ vai ''' - sitais ir sq valodā

conn.commit()

# izveidojam loga izkārtojumu- lai var redzēt GUI logā

layout=[
   [sg.T("Vards"), sg.InputText(key="vards")], 
   [sg.T("Uzvards"), sg.InputText(key="uzvards")], 
   [sg.T("Epasts"), sg.InputText(key="epasts")], 
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

# jāapskata notikums- poga :"iesniegt"
if event== "Iesniegt":
    # ir jāsavāc visi dati
    vards=values["vards"]
    uzvards=values["uzvards"]
    epasts=values["epasts"]
    
    # kā saglābāt šos datus, datu bāzē
    cursor.execute("INSERT INTO lietotaji (vards, uzvards, epasts) VALUES (?,?,?)", (vards,uzvards,epasts))
    conn.commit()



# aizvert GUI logs un datu bazes savienojums (Parbaudam ka saiet kods)
conn.close()
