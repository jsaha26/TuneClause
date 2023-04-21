#TinkerClause
from tkinter import *
from PIL import Image,ImageTk
import os
import time
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
mixer.init()

class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        # Title--
        self.root.title('TuneClause')
        
        # Width and Height--
        self.root.geometry('700x400')
        
        # resizable window off--
        self.root.resizable(0,0)

        # Backgroundcolor--
        self.root.configure(background='white')

        # openfile---
        def Openfile():
            global filename
            filename=filedialog.askopenfilename()

        # Menu-
        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)
        
        # submenu----
        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=Openfile)
        self.submenu.add_command(label='Exit',command=self.root.destroy)
       
        # For Messages--
        def About():
            tkinter.messagebox.showinfo('About Us','TuneClause by Jyotiraditya\n\nListen to your favorite tunes, with a touch of code. <>')

        self.submenu2=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Help',menu=self.submenu2)
        self.submenu2.add_command(label='About',command=About)
      
        # Adding Label---
        self.filelabel=Label(text='Select a Music',bg='black',fg='white',font=22)
        self.filelabel.place(x=5,y=30)
        
        # For path of Music
        def songinf():
            self.filelabel['text']='Current Music: ' + os.path.basename(filename)   

        # Adding leftsideimage--
        # L=Left
        self.L_photo=ImageTk.PhotoImage(file='leftsideimage.jpg')
        L_photo=Label(self.root,image=self.L_photo).place(x=260,y=80,width=500,height=250)
        
        # Adding mainimg--
        self.photo=ImageTk.PhotoImage(file='mainimg.png')
        photo=Label(self.root,image=self.photo,bg='white').place(x=5,y=60)
        
        #label-
        self.label1=Label(self.root,text="Let's Play the Music!",bg='black',fg='white',font=20)
        self.label1.pack(side=BOTTOM,fill=X)
       
        #functions-
        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text']='Music Playing...'
                    songinf()
                    length_bar()
                    
                    self.im1=ImageTk.PhotoImage(file='10.png')
                    self.im2=ImageTk.PhotoImage(file='11.png')
                    self.im3=ImageTk.PhotoImage(file='12.png')
                    # self.im4=ImageTk.PhotoImage(file='13.jpeg')
                    
                    self.imglabel=Label(self.root,bg='white')
                    self.imglabel.place(x=5,y=60)
                    
                    animation()
                
                except:
                    tkinter.messagebox.showerror('Error','File could not be found. Please try again.')
            
            else:
                mixer.music.unpause()
                
                self.imglabel=Label(self.root,bg='white')
                self.imglabel.place(x=5,y=60)
                # Animation----
                self.label1['text']='Music Playing..'   
                # self.im1=ImageTk.PhotoImage(file='12.png')
                # self.im2=ImageTk.PhotoImage(file='13.jpeg')
                self.im2=ImageTk.PhotoImage(file='10.png')
                self.im3=ImageTk.PhotoImage(file='11.png')
                self.im1=ImageTk.PhotoImage(file='12.png')

                self.imglabel=Label(self.root,bg='white')
                self.imglabel.place(x=5,y=60)
                animation()
                
        #for song length--
        def length_bar():
            #starting from Zero--
            current_time=mixer.music.get_pos()/1000
            #convert current_time in min.. and sec..
            convert_current_time=time.strftime('%M:%S',time.gmtime(current_time))
            
            #select mp3 songs--
            song_mut=MP3(filename)
            #get length of songs--
            song_mut_length=song_mut.info.length
            #convert into min. and sec.
            convert_song_mut_length=time.strftime('%M:%S',time.gmtime(song_mut_length))
            #blit on screen--
            self.lengthbar.config(text=f' {convert_current_time} / {convert_song_mut_length}')
            self.lengthbar.after(1000,length_bar)

        #label for lengthbar--
        self.lengthbar=Label(self.root,text='00:00',font=20,bg='black',fg='white')
        self.lengthbar.place(x=5,y=260)

        # Creating Buttons--
        # play_button--
        self.photo_B1=ImageTk.PhotoImage(file='3.png')
        photo_B1=Button(self.root,image=self.photo_B1,bd=0,bg='white',command=playmusic).place(x=5,y=300)        

        #function for pausebtn
        def pausemusic():
            global paused
            paused=TRUE
            mixer.music.pause()
            self.label1['text']='Music Paused'
            self.photo=ImageTk.PhotoImage(file='mainimg.png')
            photo=Label(self.root,image=self.photo,bg='white').place(x=5,y=60)

        # pause_button--
        self.photo_B2=ImageTk.PhotoImage(file='4.png')
        photo_B2=Button(self.root,image=self.photo_B2,bd=0,bg='white',command=pausemusic).place(x=85,y=300)        
        
        #function for stopbutton-
        def stopmusic():
            mixer.music.stop()
            self.label1['text']='Music Stoped'
            self.photo=ImageTk.PhotoImage(file='mainimg.png')
            photo=Label(self.root,image=self.photo,bg='white').place(x=5,y=60)
            
        # stop_button--
        self.photo_B3=ImageTk.PhotoImage(file='5.png')
        photo_B3=Button(self.root,image=self.photo_B3,bd=0,bg='white',command=stopmusic).place(x=165,y=300)        
       
        # Animation--
        def animation():
            self.im1=self.im2
            self.im2=self.im3
            # self.im3=self.im4
            self.im3=self.im1
            self.imglabel.config(image=self.im1)
            self.imglabel.after(500,animation)
            
        def mute():
            self.scale.set(0)
            self.mute=ImageTk.PhotoImage(file='mute.png')
            mute=Button(self.root,image=self.mute,command=unmute,bg='white',bd=0).place(x=280,y=290)
            self.label1['text']='Music Muted'
            
        def unmute():
            self.scale.set(30)
            self.volimg=ImageTk.PhotoImage(file='6.png')
            volimg=Button(self.root,image=self.volimg,command=mute,bg='white',bd=0).place(x=280,y=290)
            self.label1['text']='Music Playing'
        
        #volume---Img----
        self.volimg=ImageTk.PhotoImage(file='6.png')
        volimg=Button(self.root,image=self.volimg,command=mute,bg='white',bd=0).place(x=280,y=290)

        # for Volumebar ---
        def volume_(vol):
            volume= int(vol)/100
            mixer.music.set_volume(volume)
        
        #volume bar--
        self.scale=Scale(self.root,from_=0,to=100,bg='green',
                        orient=HORIZONTAL,length=120,command=volume_)
        self.scale.set(30)
        self.scale.place(x=340,y=295)  

# root=Tk()
root = tkinter.Tk()
obj=musicplayer(root)
root.mainloop()