import webbrowser
import speech_recognition as sr
from tkinter import *
from googletrans import Translator
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import threading

windows = Tk()
windows.title("pharmacy")
windows.minsize(950, 500)
windows.maxsize(950, 500)

r = sr.Recognizer()
current_line = 0


# تابع صدا گرفتن
def recognize_speech():
    global current_line
    while True:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, phrase_time_limit=30, timeout=30)
                text = r.recognize_google(audio, language='fa-IR')
                print(text)
                if text == "تمام":
                    break
                text_area.insert(INSERT, text + "\n")
                current_line = len(text_area.get(1.0, "end-1c").split("\n"))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Stopped listening")


# تابع ترجمه
def transl_btn():
    global current_line
    while True:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, phrase_time_limit=30, timeout=30)
                text = r.recognize_google(audio, language='fa-IR')
                translator = Translator()
                text = text.lower()
                v = translator.translate(text, dest="en")
                print(v.text)
                if text == "تمام":
                    break
                text_area.insert(INSERT, v.text + "\n")
                current_line = len(text_area.get(1.0, "end-1c").split("\n"))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Stopped listening")


#  تابع هنگ نکردن دکمه
def listen_in_thread():
    threading.Thread(target=recognize_speech, daemon=True).start()


def listen_in_thread2():
    threading.Thread(target=transl_btn, daemon=True).start()


# تابعی در مورد info
def information():
    try:
        info_text = webbrowser.open("https://tamin.ir/")
        print(info_text)
    except Exception as e:
        print(f"Error: {e}")


# منوی بالایی
menubar = Menu(windows)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="info", command=information)
filemenu.add_command(label="exit", command=windows.quit)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help")
windows.config(menu=menubar)

table_label2 = Label(windows, text="لیست دارو")
table_label2.place(x=840, y=10)

# تعدادی از دارو ها
List_of_medicines = [
    "بوپروپیون",
    "سیتالوپرام",
    "کلومیپرامین",
    "دسیپرامین",
    "دوکسپین",
    "دولوکستین",
    "سیتالوپراماس",
    "فلوکستین",
    "فلووکسامین",
    "ایمی پرامین",
    "ایزوکربوکسازید",
    "لیتیم کربنات",
    "ماپروتیلین",
    "میرتازاپین",
    'نفازودون',
    "نورتریپتیلن",
    'پاروکستین',
    "فنلزین سولفات",
    "پروتریپتیلین",
    'سرترالین',
    "ترانیل سیپرامین",
    "ترازودون",
    "تریمیپرامین",
    "ونلافاکسین",
    "گاما-آمینوبوتیریک اسید",
    "داپوکستین",
    "رازاگیلین"]

# اسکرول کردن نمایش دارو ها
destination_var = StringVar()
destination_combobox = ttk.Combobox(windows, textvariable=destination_var, values=List_of_medicines)
destination_combobox.grid(row=1, column=1, pady=50, padx=800)
destination_combobox.set(" ")

table_lable = Label(windows, text="نمایش دارو")
table_lable.place(x=300, y=10)
table_lable.config(font=("None", 15), fg="blue")

btn_mic = Button(windows, text="میکروفون", command=listen_in_thread)
btn_mic.config(font=("aviny", 16), bg="#808000", fg="white")
btn_mic.place(x=800, y=200)

btn_trc = Button(windows, text="translate", command=listen_in_thread2)
btn_trc.config(font=("aviny", 16), bg="blue", fg="white")
btn_trc.place(x=800, y=300)

text_area = ScrolledText(windows, wrap=WORD, width=90)
text_area.place(x=50, y=50, height=400)

windows.mainloop()
