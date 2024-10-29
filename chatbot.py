from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("650x520+0+0")
        self.root.bind('<Return>',self.enter_func)
        
        
        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack() 
        
        img_chat=Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\chatbot_images\chatbot.jpeg")
        img_chat=img_chat.resize((200,90),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)
        
        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=87,height=20,bd=9,relief=RAISED,font=('arial',10),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        
        btn_frame=Frame(self.root,bd=3,bg='white',width=730)
        btn_frame.pack()
        
        label_1=Label(btn_frame,text="Type Something",font=('arial',10,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=3,sticky=W)
        
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=62,font=('times new roman',10,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        
        
        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',11,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=3,sticky=W)
        
        
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',11,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=3,sticky=W)
        
        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',10,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=3,sticky=W)
        
    #-----------------------Function Declaration ***************************************
    
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
        
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
        
    
    def send(self):
        send='\t\t\t'+'You:  '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)
        
        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')
        
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')
            
        if (self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
            
        elif (self.entry.get()=="hi"):
            self.text.insert(END,'\n\n'+'Bot: Hello')
            
        elif (self.entry.get()=="How are you"):
            self.text.insert(END,'\n\n'+'Bot: fine and you')
            
        elif (self.entry.get()=="Fantastic"):
            self.text.insert(END,'\n\n'+'Bot: Nice to Hear')
            
        elif (self.entry.get()=="who created you"):
            self.text.insert(END,'\n\n'+'Bot: Tchorbo Douae and Terrab wiam did using python')
            
        elif (self.entry.get()=="What is your name"):
            self.text.insert(END,'\n\n'+'Bot: My name is Mr. Hacker')
        
        elif (self.entry.get()=="Can you speak French"):
            self.text.insert(END,'\n\n'+"Bot: I'm still leaning it..")
            
        elif (self.entry.get()=="What is machine learning"):
            self.text.insert(END,'\n\n'+"Bot: Machine learning is a branch\n of artificial intelligence (AI) that involves developing algorithms and statistical models that enable computer systems to learn from data and make predictions or decisions without being explicitly programmed for each individual task.")
        
        elif (self.entry.get()=="How does face recognition work?"):
            self.text.insert(END,'\n\n'+"Bot: Face recognition is a computer technology that uses machine learning algorithms to automatically identify and verify individuals based on their facial features.")
       
        elif (self.entry.get()=="How does face recognition work step by step?"):
            self.text.insert(END,'\n\n'+"Bot: Here is a high-level \noverview of how face recognition works:\n Face detection: The system first detects and locates human faces \nwithin an image or video frame using various techniques \nsuch as the Haar cascade classifier or deep learning-based methods \nlike Convolutional Neural Networks (CNN).\n Feature extraction: Once the faces are detected,\n the system extracts a set of unique features \nfrom the face such as the distance between the eyes,\n the shape of the nose,\n and the depth of the eye sockets. \n Face matching: The face template is then compared \nto a database of known faces to determine\n if the person has been previously identified or not. \nIdentification or Verification: Depending on the specific use case, \nface recognition systems can either\n perform identification or verification. \n Continuous learning: Modern face recognition systems \ncan learn continuously by updating \ntheir models with new data,\n which helps improve their accuracy \nand robustness over time.")
        
        elif (self.entry.get()=="what is python programming?"):
            self.text.insert(END,'\n\n'+"Bot: Python is a high-level, \ninterpreted programming language that was first released in 1991 by Guido van Rossum. \nIt is designed to be easy to read and write, \nwith a simple and clear syntax, \nmaking it an ideal language for beginners to learn. \nPython is widely used for a variety of purposes,\n including web development,\n scientific computing, \ndata analysis, \nartificial intelligence,\n and machine learning,\n among others.")
            
        elif (self.entry.get()=="What is chatbot?"):
            self.text.insert(END,'\n\n'+"Bot: A chatbot is a software program \nthat is designed to interact\n with humans through a conversational interface, \nsuch as text chat, \nvoice, \nor messaging platforms")
       
       
        elif (self.entry.get()=="bye"):
            self.text.insert(END,'\n\n'+'Bot: Thank you for Chatting')
            
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it")
            
        
            
        



if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
    
