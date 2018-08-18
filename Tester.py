from tkinter import *
from  tkinter import filedialog



root = Tk()

root.filename  = filedialog.askopenfilename(initialdir='/', title='Select a file to open', filetypes=(('text files', '*.txt'), ('all files', '*.*')))
# a = root.filename.replace('/', r'\\')

a = root.filename
aa = a.split('.')

print(aa)




root.mainloop()