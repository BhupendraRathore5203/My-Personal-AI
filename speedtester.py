from tkinter import *
import speedtest
# **********************************************************************
# Function to get the upload and download speeds

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3))+ "Mbps"
    up = str(round(sp.upload()/(10**6), 3))+ "Mbps"
    lab_down.configure(text=down)
    lab_up.configure(text=up)

# **********************************************************************
sp = Tk()
sp.title("Internet Speed")
sp.geometry("500x500")
sp.configure(bg = "grey")

lab = Label(sp, text= "Internet Speed Tester", font=("Time New Roman", 25, "bold", "italic"), bg= "grey", fg="black")
lab.place(x=60, y=60, height="30", width="380")

lab = Label(sp, text= "Download Speed", font=("Time New Roman", 20, "bold", "italic"), bg= "grey", fg="black")
lab.place(x=60, y=180, height="30", width="380")

lab_down = Label(sp, text= "00", font=("Time New Roman", 20, "bold", "italic"), bg= "grey", fg="black")
lab_down.place(x=60, y=220, height="30", width="380")

lab = Label(sp, text= "Upload Speed", font=("Time New Roman", 20, "bold", "italic"), bg= "grey", fg="black")
lab.place(x=60, y=310, height="30", width="380")

lab_up = Label(sp, text= "00", font=("Time New Roman", 20, "bold", "italic"), bg= "grey", fg="black")
lab_up.place(x=60, y=350, height="30", width="380")

button = Button(sp, text="Check Speed", font=("Time New Roman", 13, "bold", "italic",), relief=RAISED, bg = "green", fg="black", command=speedcheck)
button.place(x=60, y=400, height="30", width="380")

sp.mainloop()