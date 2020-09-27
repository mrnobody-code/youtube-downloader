from distutils import command

from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *

file_size = 0


def download():
    global file_size
    try:
        url = urlField.get()
        # Chaning button
        dBtn.config(text='Please Wait...')
        dBtn.config(state=DISABLED)
        path = askdirectory()
        if path is None:
            return

        ob = YouTube(url)
        strms = ob.streams.first()
        file_size = strms.filesize

        print(file_size)
        print(strms)
        strms.download(path)
        print("done..")
        dBtn.config(text="Start")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Download Successfully..")
        urlField.delete(0, END)

    except Exception as e:
        print(e)
        print("Error Occured")


def stdDownThread():
    thread = Thread(target=download)
    thread.start()


# Starting gui building
root = Tk()

root.title("Youtube Downloader")
root.iconbitmap('youtube.ico')
root.geometry("300x200")
# file=PhotoImage(file="youtube.png")
# headIcon=Label(main,image=file)
# headIcon.pack(side=TOP)
urlField = Entry(root, font=('consolas', 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10, pady=20)

dBtn = Button(root, text="start", font=("consolas", 10), justify=CENTER, relief="ridge", command=stdDownThread)
dBtn.pack(side=TOP, pady=10)
root.mainloop()
