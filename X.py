from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# ***********************************************************************************************************************
# МЕТОДЫ И ФУНКЦИИ
# ***********************************************************************************************************************

# Рассположение лошадей на экране
def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)

# Добавление строки в текстовый блок textDiary
def insertText(s):
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)

# Копируем и всавляем функцию load Money и метод save Money из КАЗИНО
def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m


# Запись суммы в файл
def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла наше КАЗИНО закрывается!")
        quit(0)
def getValues(summa):
    value = []
    if summa > 9:
        for i in range(0, 11):
            value.append(i*(int(summa) // 10))
        else:
            value.append(0)
            if summa > 0:
                value.append(summa)
        return value

root = Tk()
# ***********************************************************************************************************************
# ЗНАЧЕНИЯ ПЕРЕМЕННЫХ
# ***********************************************************************************************************************
# Размеры окна
WIDTH = 1040
HEIGHT = 650

# Позиции лошадей
x01 = 20
x02 = 20
x03 = 20
x04 = 20

defaultMoney = 10000
money = 0
valuta = "руб"

nameHorse01 = "Ананас"
nameHorse02 = "Сталкер"
nameHorse03 = "Обжора"
nameHorse04 = "Осел"

summ01 = intVar()
summ02 = intVar()
summ03 = intVar()
summ04 = intVar()

# ***********************************************************************************************************************
# ФОРМИРОВАНИЕ ЭЛЕМЕНТОВ В ОКНЕ
# ***********************************************************************************************************************
# Создаем главное окно
# Вычисление и присваивание координат точке отсчета окна

POS_X = root.winfo_screenwidth()//2 - WIDTH // 2

POS_Y = root.winfo_screenheight()//2 - HEIGHT // 2

root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# Установка заголовка
root.title("RACETRACK")

# Запрет исменения размеров пользователем
root.resizable(False, False)

# загрузка беговой трассы
road_image = PhotoImage(file="road.png")
road = Label(root, image=road_image)
road.place(x=0, y=17)

# Загрузка изображения лошадей
horse01_image = PhotoImage(file="horse01.png")  # Загрузка изображения лошади 01
horse01 = Label(root, image=horse01_image)  # Установка  в Lable

horse02_image = PhotoImage(file="horse02.png")  # Загрузка изображения лошади 02
horse02 = Label(root, image=horse02_image)  # Установка  в Lable

horse03_image = PhotoImage(file="horse03.png")  # Загрузка изображения лошади 03
horse03 = Label(root, image=horse03_image)  # Установка  в Lable

horse04_image = PhotoImage(file="horse04.png")  # Загрузка изображения лошади 04
horse04 = Label(root, image=horse04_image)  # Установка  в Lable

horsePlaceInWindow()

# Создаем кнопку и выводим на экран
startButton = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")
startButton.place(x=20, y=370)

# Информационный чат
textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)

scroll = Scrollbar(command=textDiary.yvaiew, width=20)
scroll.place(x=990, y=450, height=132)
textDiary["yscrollcommand"] = scroll.set

money = loadMoney()

if money <= 0:
    messagebox.showinfo("Стоп!","На ИППОДРОМ без средств заходить нельзя!")
    quit = (0)

LabelAllMoney = Label(text=f"Осталось средств: {money} {valuta}.", font="Arial 12")
LabelAllMoney.place(x=20, y=565)

#Вывод текста со ставками на лошадь
LabelHorse01 = Label(text="Ставка на лошадь №1")
LabelHorse01.place(x=20, y=480)

LabelHorse02 = Label(text="Ставка на лошадь №2")
LabelHorse02.place(x=20, y=510)

LabelHorse03 = Label(text="Ставка на лошадь №3")
LabelHorse03.place(x=20, y=450)

LabelHorse01 = Label(text="Ставка на лошадь №4")
LabelHorse01.place(x=20, y=540)

#Вывод чекбоксов
horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)

#Выпадающий список (drop-dawn list)
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

# Делаем атрибут "только чтение" (Make an attribute "read-only")
stavka01["state"] = "readonly"
stavka01.place(x=280, y=450)

stavka02["state"] = "readonly"
stavka02.place(x=280, y=480)

stavka03["state"] = "readonly"
stavka03.place(x=280, y=510)

stavka04["state"] = "readonly"
stavka04.place(x=280, y=540)

stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

refreshCombo("")
root.mainloop()