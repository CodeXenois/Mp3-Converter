from tkinter import *
import moviepy.editor
from tkinter.filedialog import *

video = ""
location = ""
name = ""

H = 250
W = 500

root = Tk()
root.title("Mp3 Converter")
root.resizable(0,0)

def file_name():
    global video
    video_name = askopenfilename()
    video = moviepy.editor.VideoFileClip(video_name)
    label = Label(canvas, text=video_name, font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white",anchor="nw",justify="left")
    label.place(relx=0.25, rely=0.3, relheight=0.1, relwidth=0.7)

def location_name():
    global location
    location = askdirectory()
    label = Label(canvas, text=location, font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white", anchor="nw",justify="left")
    label.place(relx=0.25, rely=0.5, relheight=0.1, relwidth=0.7)
    convert_button = Button(canvas, text="Convert File", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white",command=lambda:Convert(name_entry.get()))
    convert_button.place(relx=0.5, rely=0.7, relheight=0.1, relwidth=0.2)

def Convert(NAME):
    global name
    name = NAME
    audio = video.audio
    audio.write_audiofile(location + "/" + name+".mp3")
    print(name)
    print("Completed")


canvas = Canvas(root, height=H, width=W,bg="white")
canvas.pack()

name_label = Label(canvas, text="Name: ", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white")
name_label.place(relx=0.01, rely=0.1, relheight=0.1, relwidth=0.2)

name_entry = Entry(canvas,font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white")
name_entry.place(relx=0.25, rely=0.1, relheight=0.1, relwidth=0.2)

file_button = Button(canvas, text="Choose File", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white",
                     command=lambda: file_name())
file_button.place(relx=0.01, rely=0.3, relheight=0.1, relwidth=0.2)

location_button = Button(canvas, text="Choose Location", font=("Bahnschrift SemiBold", 10), bg="#353333", fg="white",
                         command=lambda: location_name())
location_button.place(relx=0.01, rely=0.5, relheight=0.1, relwidth=0.2)

credit_label = Label(canvas, text="Kevin's First Working App", font=("Bahnschrift SemiBold", 10), bg="white", fg="#353333",anchor="nw",justify="left")
credit_label.place(relx=0.01, rely=0.9, relheight=0.1, relwidth=0.5)


root.mainloop()