from moviepy.video.io.VideoFileClip import VideoFileClip
from pytube import YouTube
import moviepy.editor
from tkinter import *
from tkinter.filedialog import *

H = 500
W = 750

root = Tk()
root.title("MyApp")
root.resizable(0,0)

canvas = Canvas(root, height=H, width=W,bg="white")
canvas.pack()

def Download_vid():
    location = askdirectory()
    url = YT_entry.get()
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    print(location)
    video.download(location)

def Convert_Mp3():
    print("Hi")
    file_name = askopenfilename()
    new_name = asksaveasfilename()
    video = VideoFileClip(file_name)
    audio = video.audio
    audio.write_audiofile(new_name + ".mp3")
    

YT_Title_label = Label(canvas, text="Youtube Converter ", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white")
YT_Title_label.place(relx=0.05, rely=0.03, relheight=0.05, relwidth=0.2)

YT_label = Label(canvas, text="URL: ", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white")
YT_label.place(relx=0.05, rely=0.1, relheight=0.05, relwidth=0.1)

YT_entry = Entry(canvas,font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white")
YT_entry.place(relx=0.175, rely=0.1, relheight=0.05, relwidth=0.35)

YT_button = Button(canvas, text="Download", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white",command=lambda:Download_vid())
YT_button.place(relx=0.55, rely=0.1, relheight=0.05, relwidth=0.1)

MP3_Title_label = Label(canvas, text="MP3 Converter ", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white")
MP3_Title_label.place(relx=0.05, rely=0.2, relheight=0.05, relwidth=0.2)

MP3_Label = Label(canvas, text="Pick File: ", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white")
MP3_Label.place(relx=0.05, rely=0.27, relheight=0.05, relwidth=0.1)

MP3_button = Button(canvas, text="Convert", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white",command=lambda:Convert_Mp3())
MP3_button.place(relx=0.175, rely=0.27, relheight=0.05, relwidth=0.1)

root.mainloop()
