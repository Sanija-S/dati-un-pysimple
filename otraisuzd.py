import PySimpleGUI as sg
import sqlite3


conn=sqlite3.connect("datubaze.db") 
cursor=conn.cursor()



cursor.execute(""" CREATE TABLE IF NOT EXISTS lietotaji(
               ID INTEGER PRIMARY KEY ,
               vards TEXT,
               uzvards TEXT,
               epasts TEXT
               
)""") 

conn.commit()


def iegut_liet_datus():
    cursor.execute("SELECT * FROM lietotaji")
    return cursor.fetchall() # atgriez VISUS datus(visas rindinas ar pēdejo sql)- jauzmanas ja datu apjoms ir LIELS
def pievienot_lietotaju (vards, uzvards, epasts):
     cursor. execute("INSERT INTO lietotaji (vards, uzvards, epasts) VALUES (?,?,?), (vards,uzvards,epasts)")
     conn.commit()

layout=[
   [sg.T("Vārds"), sg.InputText(key="vards")], 
   [sg.T("Uzvārds"), sg.InputText(key="uzvards")], 
   [sg.T("Epasts"), sg.InputText(key="epasts")], 
   [sg.Button("Iesniegt"), sg.Button("Dzēst izvēli"), sg.Button("Iziet")],
   [sg.Table(values=iegut_liet_datus(), headings=["ID", "Vārds", "Uzvārds", "Epasts"], key="tabula", enable_events=True, bind_return_key=True)]# nav datu lauku nosaukumi- so var ar garumzimem

]

logs=sg.Window("Datu bāze").Layout(layout)# cits pieraksts....

""" or...
while True: 
    event,values=logs.read()
    if event ==sg.WIN_CLOSED or event=="Iziet":
        break
"""
while True: 
    event,values=logs.read()
    if event is None or event=="Iziet":
        break
if event== "Iesniegt":
    vards=values["vards"]
    uzvards=values["uzvards"]
    epasts=values["epasts"]
    
    if vards and uzvards and epasts:
       pievienot_lietotaju(vards, uzvards, epasts)
       logs.Element("tabula").Update(values=iegut_liet_datus()) # ar mazo burtu- atslega tabulai(konkrets) , ar lielo burtu- jebkurai vertibai ar citm tabulam (attiecas uz visu)
       
       logs["vards"].update("") #notīra visu9(sitas 3 lines)
       logs["uzvards"].update("")
       logs["epasts"].update("")


conn.close()