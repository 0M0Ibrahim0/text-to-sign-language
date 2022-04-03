from Tkinter import *
import tst
import os
root =Tk()
root.geometry("1300x500")
m= PhotoImage(file = "sign.gif")
C = Canvas(root, bg="blue", height=700 , width = 700)
bac=PhotoImage(file = "w.gif")
photoimage= bac.subsample(9,9)
background_label = Label(root, image=m)
background_label.place(x=0, y=0, relwidth= 1, relheight=1)

#*********** lable
'''
photoimage1= bac.subsample(1,1)
lrate = StringVar()
lratel2 = Label(root, textvariable=lrate  ,font = ('calibri', 14, 'bold'),  image = photoimage ,compound = CENTER)
lrate.set("RUN")
lratel2.place(x=900, y=70)
'''
#***************
#textbox
#**************************
entry1 = Entry (root)
C.create_window(300, 140,height=30,width=500, window=entry1)

#************************
# Run Button
#********************
def run():
    #os.system('Anim_Talking_1.fbx')
    text = entry1.get() # text box
    tst.getseq(text)
    entry1.delete(0,END)

Image2 = PhotoImage(file = "w.gif")
B2 = Button(root, font = ('calibri', 14, 'bold'),text=" Translate " ,height=1,width=9 ,command=run )
B2.place(x=900, y=120)
#**********************

# button background
#*****************
def run_Bwellcom():
    B4.destroy()

Image4 = PhotoImage(file = "s.gif")
B4 = Button(root,image =Image4   ,height=500,width=1300 ,command=run_Bwellcom )
B4.place(x=0, y=0)
#**************************



C.pack()

root.mainloop()


