from counter import Counter
from tkinter import *

def update_label():
	global txt_var

	try:
		lbl.configure(text=str(counter.get_count()))
	except:
		pass

def new():
	global counter
	
	try:
		counter = Counter() if txt.get() == "" else Counter(int(txt.get()))
		update_label()
	except ValueError:
		pass

def incr():
	if counter is None:
		return
	counter.incr()
	update_label()

def decr():
	if counter is None:
		return
	counter.decr()
	update_label()

if __name__ == "__main__":
	counter = None

	window = Tk()
	window.title("Welcome to Counter")

	lbl = Label(window, text="N/A")
	txt = Entry(window, width=10)
	btn_new = Button(window, text="new", command=new)
	btn_incr = Button(window, text="incr", command=incr)
	btn_decr = Button(window, text="decr", command=decr)

	lbl.pack()
	txt.pack()
	btn_new.pack()
	btn_incr.pack()
	btn_decr.pack()

	window.mainloop()