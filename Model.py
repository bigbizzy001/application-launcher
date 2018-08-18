import subprocess

apps = {'UCBrowser': "C:\\Program Files (x86)\\UCBrowser\\Application\\UCBrowser.exe",
            'Pycham': "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2017.2.4\\bin\\pycharm64.exe",
            'Cmder': 'C:\\Users\\marcus\\Desktop\\cmder_mini\\Cmder.exe',
            'IDLE': "C:\\Users\\marcus\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\idlelib\\idle.pyw",
            'Code Blocks': "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe",
            'Adobe Reader': "C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe"
        }


def single_open(filename, extension):
    if extension == 'docx' or extension == 'doc':
        subprocess.Popen(["C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE", filename])
    else:
        subprocess.Popen(['Start', filename], shell=True)


# single_open('C:\\Users\\marcus\\Desktop\\CBM Paper reviewed.docx')

def launcher(location):
    subprocess.Popen(apps[location])


def openIdle():
    subprocess.Popen(['Start', apps['IDLE']], shell=True)



# subprocess.Popen("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE")