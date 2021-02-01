
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from webbrowser import open as openn
from tkinter.filedialog import*
#Functions
def internetRU(event):#функция открытия браузера
    url=openn('https://ushakovdictionary.ru/search.php')
def internetEN(event):#функция открытия браузера
    url=openn('https://www.dictionary.com/')

def read_file(f):
    file=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in file:
        mas.append(rida.strip())
    file.close()
    print(mas)
    return mas

def translate(event):
    text=ent2.get()
    if text in rus:
        lalR.configure(text=f'{text}-{eng[rus.index(text)]}')
    else:
        lalR.configure(text=f'{text} - {rus[eng.index(text)]}')

def add_new(event):
    text=ent4.get()
    text2=ent5.get()
    ru=list(map(ord,list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')))
    en=list(map(ord,list('abcdefghiklmnopqrstvxyz')))
    text1=list(map(ord,list(text)))
    check = 0
    for i in text1:
        if i in en:
            check+=1
        if check == len(text1):
            eng.append(text)
            rus.append(text2)
            with open(r"Eng.txt", "a",encoding="utf-8-sig") as file:
                file.write(text + '\n')
            with open(r"Rus.txt", "a",encoding="utf-8-sig") as file:
                file.write(text2 + '\n')
    check1=0
    for i in text1:
        if i in ru:
            check1+=1
        if check1==len(text1):
            rus.append(text)
            eng.append(text2)
            with open(r"Rus.txt", "a",encoding="utf-8-sig") as file:
                file.write(text + '\n')
            with open(r"Eng.txt", "a",encoding="utf-8-sig") as file:
                file.write(text2 + '\n')
    ent4.delete(0,END)
    ent5.delete(0,END)

def change (event):
    text=ent6.get()
    text2=ent7.get()
    if text in rus:
      ind=rus.index(text)
      j=eng[ind]
      rus.remove(text)
      rus.append(text2)
      eng.remove(j)
      eng.append(j)
      file=open(r"Rus.txt", "r+",encoding="utf-8-sig")
      file.write(text2 + '\n')
      file.close()
      file=open(r"Eng.txt", "r+",encoding="utf-8-sig")
      file.write(j + '\n')
      file.close ()
    elif text in eng:
      ind=eng.index(text)
      j=rus[ind]
      eng.remove(text)
      eng.append(text2)
      rus.remove(j)
      rus.append(j)
      file=open(r"Eng.txt", "r+",encoding="utf-8-sig")
      file.write(text2 + '\n')
      file.close()
      file=open(r"Rus.txt", "r+",encoding="utf-8-sig")
      file.write(j + '\n')
      file.close ()
    ent6.delete(0,END)
    ent7.delete(0,END)

#Window
win=Tk()
win.title('Словарь. Dictionary.')
win.geometry('800x800')
tab_control=ttk.Notebook(win)
tab1=Frame(tab_control)
tab2=Frame(tab_control)
tab3=Frame (tab_control)
tab_control.add(tab1,text="Толковый словарь")
tab_control.add(tab2,text="Перевод")
tab_control.add(tab3,text="Редактировать")
tab_control.pack(expand=1,fill='both')
#TAB1 lbl btn 
lbl=Label(tab1,text='Здесь можно посмотреть значения слов в толковом словаре. \nHere you can check words meaning in in the definition dictionary',font='arial 12')
lbl.grid(row=0,column=0,columnspan=3)
lbl1=Label(tab1,text='Нажав на кнопку вы попадёте на страницу словаря Ушакова',font='arial 10')
lbl1.grid(row=1,column=0,columnspan=1)
btn1=Button(tab1,text='Словарь Ушакова',font='arial 10')
btn1.grid(row=1,column=2)
btn1.bind("<Button-1>",internetRU)
lbl2=Label(tab1,text='When you click the Button, you will be directed to the definition dictionary',font='arial 10')
lbl2.grid(row=2,column=0,columnspan=1)
btn2=Button(tab1,text='Dictionary.com',font='arial 10')
btn2.grid(row=2,column=2)
btn2.bind("<Button-1>",internetEN)

#TAB2 lal bon ent RUS
lal2=Label(tab2,text='Здесь можно узнать перевод слов.',font='arial 12')
lal2.grid(row=0,column=0, columnspan=3)
lal1=Label(tab2,text='Введите слово',font='arial 10')
lal1.grid(row=1,column=0)
lalR=Label(tab2,text="Здесь будет перевод",font='arial 10')
ent2=Entry(tab2,width=30)
ent2.grid(row=1,column=1)
bon2=Button(tab2,text='Перевод',font='arial 10')
bon2.grid(row=1,column=2)
bon2.bind('<Button-1>', translate)
lalR.grid(row=3,column=1)


#TAB3 lal ent bon ENG
lal3=Label(tab3,text='Здесь можно добавить или изменить слово',font='arial 12')
lal3.grid(row=0,column=0, columnspan=3)
lal6=Label(tab3,text='Введите новое слово ',font='arial 10')
lal6.grid(row=1,column=0)
ent4=Entry(tab3, width=30)
ent4.grid(row=1,column=1)
lal7=Label(tab3,text='Перевод',font='arial 10')
lal7.grid(row=2,column=0)
ent5=Entry(tab3, width=30)
ent5.grid(row=2,column=1)
bon5=Button(tab3, text='Сохранить', font='arial 10')
bon5.grid(row=2, column=2)
bon5.bind('<Button-1>', add_new)
lal8=Label(tab3,text='Введите неверное слово ',font='arial 10')
lal8.grid(row=3,column=0)
ent6=Entry(tab3, width=30)
ent6.grid(row=3,column=1)
lal9=Label(tab3,text='Введите верное слово ',font='arial 10')
lal9.grid(row=4,column=0)
ent7=Entry(tab3, width=30)
ent7.grid(row=4,column=1)
bon7=Button(tab3, text='Изменить', font='arial 10')
bon7.grid(row=4, column=2)
bon7.bind('<Button-1>', change)

rus=[]
eng=[]
rus=read_file("rus.txt")
eng=read_file('eng.txt')

win.mainloop()