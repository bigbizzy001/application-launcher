from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import Model



root = Tk()
root.title('Application Launcher')
root.geometry('730x300')
root.config(bg='powder blue')
root.iconbitmap('marcus.ico')

var = StringVar()

def openApps(n):
    Model.launcher(n)


def openAppIdle():
    Model.openIdle()


def openfile():
    file = filedialog.askopenfilename(initialdir='/', title='Select a file to open',
            filetypes=(('text files', '*.txt'), ('all files', '*.*')))
    # fileNameEntry.config(text=file)
    var.set(file)
    # print(var.get())


def launchApps():
    filename = var.get().replace('/', r'\\')
    a = var.get().split('.')
    extension = a[1]
    print(filename)
    print(extension)
    Model.single_open(filename, extension)
    print(filename)

singleApp = Frame(root, bg='powder blue')
fileChoose = Label(singleApp, text='Choose file to open', bg='powder blue')
fileChoose.grid(row=0, column=0)

fileNameEntry = Label(singleApp, width=70, textvariable=var)
fileNameEntry.grid(row=0, column=1)

fileChooser = Button(singleApp, text=':', command=openfile)
fileChooser.grid(row=0, column=2, padx=5)

launchApp = Button(singleApp, text='LAUNCH APP', command=launchApps)
launchApp.grid(row=0, column=3)

apps = Frame(root, bg='powder blue')
appsLabelFrame = LabelFrame(apps, text='Launcher', bg='powder blue')

UCBrowser = Button(appsLabelFrame, text='UCBrowser', width=15, height=6, command=lambda: openApps('UCBrowser'))
UCBrowser.grid(row=0, column=0)

Pycham = Button(appsLabelFrame, text='Pycham', width=15, height=6, command=lambda:openApps('Pycham'))
Pycham.grid(row=0, column=1)

Cmder = Button(appsLabelFrame, text='Cmder', width=15, height=6, command=lambda:openApps('Cmder'))
Cmder.grid(row=0, column=2)

IDLE = Button(appsLabelFrame, text='IDLE', width=15, height=6, command=openAppIdle)
IDLE.grid(row=0, column=3)

codeBlocks = Button(appsLabelFrame, text='Code Blocks', width=15, height=6, command=lambda:openApps('Code Blocks'))
codeBlocks.grid(row=0, column=4)

windowsMediaPlayer = Button(appsLabelFrame, text='Windows Media Player', width=15, height=6, command=openApps)
windowsMediaPlayer.grid(row=0, column=5)

AdobeReader = Button(appsLabelFrame, text='Adobe Reader', width=15, height=6, command=lambda:openApps('Adobe Reader'))
AdobeReader.grid(row=0, column=5)


appsLabelFrame.pack()
singleApp.pack(pady=10)
apps.pack()
root.mainloop()