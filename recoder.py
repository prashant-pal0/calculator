import sounddevice as sd
import soundfile as sf
from tkinter import *
def voice_rec():
    fs = 48000
    # seconds
    duration = 60
    myrecording = sd.rec(int(duration * fs),samplerate=fs, channels=2)

    sd.wait()
    return sf.write('my_Audio_file.flac', myrecording, fs)
def rec_stop():

    fs = 48000
    myrecording = sd.stop(samplerate=fs, channels=2)

    sd.wait()
    return sf.write('my_Audio_file.flac', myrecording, fs)

master = Tk()

Label(master, text="voice recoder : ").grid(row=0, sticky=W, rowspan=5)

b= Button(master, text="start",command=voice_rec, bg="red", fg="white")
b.grid(row=0, column=2, columnspan=10, rowspan=2,padx=5, pady=5)
b1 = Button(master, text="stop",bg=r"red",fg="white",command=rec_stop)
b1.grid(row=0,column=30, columnspan=2,padx=5, pady=5)
mainloop()


