# write_app.py
import mmap
from Tkinter import *

class WriteApp:
	mmap_file = None
	def __init__(self, master):
		self.master = master
		self.master.title('mmap demo')
		
		frm = Frame(self.master)
		frm.pack()
		
		self.open_button = Button(frm, text = 'Create a mmap', command = self.create_mmap)
		self.open_button.pack(side = LEFT)
		
		self.close_button = Button(frm, text = 'Close a mmap', state = DISABLED, command = self.close_mmap)
		self.close_button.pack(side = LEFT)
		
		self.text = Entry(frm)
		self.text.pack(side = BOTTOM)
		self.text.bind('', self.write_text)
		self.text.config(state = DISABLED)
		
	def create_mmap(self):
		self.mmap_file = mmap.mmap(0, 1024, access = mmap.ACCESS_WRITE, tagname = 'share_mmap')
		self.close_button.config(state = ACTIVE)
		self.open_button.config(state = DISABLED)
		self.text.config(state = NORMAL)
		
	def close_mmap(self):
		self.close_button.config(state = DISABLED)
		self.open_button.config(state = ACTIVE)
		self.text.config(state = DISABLED)
		self.mmap_file.close()
		
	def write_text(self, event):
		txt = self.text.get()
		self.mmap_file.write(txt)
		self.text.delete(0, len(txt))

if __name__ == '__main__':
	root = Tk()
	app = WriteApp(root)
	root.mainloop()