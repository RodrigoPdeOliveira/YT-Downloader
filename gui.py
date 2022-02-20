from tkinter import *
from tkinter import ttk
import downloader


def get_links():
    links = link_text.get('1.0', END)
    links = links.split('\n')
    links.remove('')
    return links


def clear_links():
    link_text.delete('1.0', END)


def mp3_dl():
    links = get_links()
    downloader.mp3(links)


def mp4_dl():
    links = get_links()
    downloader.mp4(links)


root = Tk()
root.title('Youtube Downloader')
root.resizable(0, 0)
# root.geometry('650x350')

mainframe = ttk.Frame(root, padding=10)
mainframe.grid()

link_lbl = ttk.Label(mainframe, text='Link(s):', padding='0 0 10').grid(column=0, row=0, columnspan=1)
link_text = Text(mainframe, width=50, height=10)
link_text.grid(column=1, row=0, columnspan=4)

mp3_dl = ttk.Button(mainframe, text='Download MP3', command=mp3_dl).grid(column=1, row=2, sticky=EW)
mp4_dl = ttk.Button(mainframe, text='Download MP4', command=mp4_dl).grid(column=2, row=2, sticky=EW)
clear_links = ttk.Button(mainframe, text='Clear links', command=clear_links).grid(column=3, row=2, sticky=EW)
quit_button = ttk.Button(mainframe, text='Quit', command=quit).grid(column=4, row=2, sticky=EW)

root.mainloop()
