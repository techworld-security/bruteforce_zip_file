#!/usr/bin/python

from zipfile import ZipFile
from tkinter import *
from tkinter import ttk
import time



class MyWindow:
	def __init__(self, win):
		self.lbl1 = Label (win, text= ' Enter the file path of zip file')
		self.lbl3=Label(win, text='password')
		self.t1=Entry()
		self.t3=Entry()
		self.lbl1.place(x=10, y=50)
		self.t1.place(x=200, y=50)
		self.b1=Button(win, text='Go', command=lambda: [self.main(), self.step()])
		self.lbl3.place(x=10, y=200)
		self.t3.place(x=200, y=200, width=180)
		self.b1.place(x=160, y=100)
		self.progress = ttk.Progressbar(win, orient=HORIZONTAL, length=300, mode='determinate')
		self.progress.place(x= 55, y=150)

	def main(self):
		self.t3.delete(0, "end")
		filename = self.t1.get()
		dictionary = 'rockyou.txt'
		password = None
		with open(dictionary, 'rb') as f:
			for line in f.readlines():
				password = line.strip()
				with ZipFile(filename)as zf:
					try:
						zf.extractall(pwd=password)
						self.t3.insert(0, password.decode().strip())
						break
					except:
						pass

	def step(self):
		for x in range(5):
			self.progress['value'] +=50
#			self.progress.update()
			time.sleep(1)

window=Tk()
mywin=MyWindow(window)
window.title('Zip cracker')
window.geometry("400x300+10+10")
window.mainloop()
