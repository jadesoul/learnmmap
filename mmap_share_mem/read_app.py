# read_app.py
from Tkinter import *
import mmap

class ReadApp:
	mmap_file = None
	def __init__(self, master):
		self.master = master
		self.master.title('read mmap')
		
		frm = Frame(self.master)
		frm.pack()
		
		self.refresh_button = Button(frm, text = 'Refresh mmap content', command = self.refresh_mmap)
		self.refresh_button.pack(side = TOP)
		
		self.text_variable = StringVar()
		self.text = Label(frm, textvariable = self.text_variable)
		self.text.pack(side = BOTTOM)
	
	def refresh_mmap(self):
		if not self.mmap_file:
			self.mmap_file = mmap.mmap(-1, 1024, access = mmap.ACCESS_READ, tagname = 'share_mmap')
		self.mmap_file.seek(0)	
		self.text_variable.set(self.mmap_file.readline())
		
if __name__ == '__main__':
	root = Tk()
	app = ReadApp(root)
	root.mainloop()