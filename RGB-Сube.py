from tkinter import *
k=128
rbc=[[0,1,2],[2,0,1],[1,2,0]]
def hexcollor(n=0):
    c=str(hex(n%16777216))[2:]
    return '#'+str(0)*(6-len(c))+c
def draw(event):
    global k
    k=s.get()
    c.delete("all")
    for i in range(256):
        for j in range(256):
            c.create_rectangle(3*i+2,3*j+2,3*i+5,3*j+5,fill=hexcollor((i%256)*256**rbc[rb.get()][0]+(j%256)*256**rbc[rb.get()][1]+(k%256)*256**rbc[rb.get()][2]),width=0)
def search(event):
    for i in range(len(str(event))):
        if(str(event)[i:i+2]=='x='):
            d=str(event)[i+2:-1]
            break
    for i in range(len(d)):
        if(d[i]==' '):
            x=int(d[:i])
    for i in range(len(d)):
        if(d[i]=='='):
            y=int(d[i+1:])
    x,y=x//3,y//3
    l["text"]='Колір: '+hexcollor(min(x,255)*256**rbc[rb.get()][0]+min(y,255)*256**rbc[rb.get()][1]+k*256**rbc[rb.get()][2])
    c1["bg"]=hexcollor(min(x,255)*256**rbc[rb.get()][0]+min(y,255)*256**rbc[rb.get()][1]+k*256**rbc[rb.get()][2])
My_window=Tk()
My_window.title("+&×")
My_window.geometry("772x868")
My_window["bg"]="#ffffff"
c=Canvas(My_window,width=768,height=768,bg='#ffffff')
c.place(x=0,y=0)
c1=Canvas(My_window,width=25,height=25,bg='#808080')
c1.place(x=700,y=836)
rb=IntVar()
Radiobutton(My_window,text='Зріз по червоному R',variable=rb,value=0,font=16,bg='#ffffff').place(x=5,y=836)
Radiobutton(My_window,text='Зріз по зеленому G',variable=rb,value=1,font=16,bg='#ffffff').place(x=208,y=836)
Radiobutton(My_window,text='Зріз по синіму B',variable=rb,value=2,font=16,bg='#ffffff').place(x=400,y=836)
l=Label(My_window,text='Колір: #808080',fg="#000000",bg="#ffffff",justify=LEFT,font=150)
l.place(x=580,y=838)
s=Scale(My_window,orient=HORIZONTAL,length=764,from_=0,to=255,tickinterval=15,resolution=1,bg='#ffffff')
s.place(x=1,y=772)
rb.set(2)
s.set(k)
k=s.get()
draw(k)
s.bind('<Button-3>',draw)
c.bind('<Button-1>',search)
My_window.mainloop()