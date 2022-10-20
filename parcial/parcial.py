from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Radiobutton, IntVar


#Se crean la ventana y su dimensión
vent1= Tk()
vent1.geometry("500x500")


#Se agregan las imagenes que se muestran en el menu
image1 = Image.open("carne.jpg")
image1= image1.resize((50,50), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image1)
image1 = Label(vent1, image = img)


image2 = Image.open("pollo.jpg")
image2= image2.resize((50,50), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(image2)
image2 = Label(vent1, image = img2)

image3 = Image.open("lasaña.jpg")
image3= image3.resize((50,50), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(image3)
image3 = Label(vent1, image = img3)


image4 = Image.open("ensalada.jpg")
image4= image4.resize((50,50), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(image4)
image4 = Label(vent1, image = img4)

image5 = Image.open("coditos.jpg")
image5 = image5.resize((50,50), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(image5)
image5 = Label(vent1, image = img5)

image6 = Image.open("rusa.jpg")
image6 = image6.resize((50,50), Image.ANTIALIAS)
img6 = ImageTk.PhotoImage(image6)
image6 = Label(vent1, image = img6)

image7 = Image.open("soda.jpg")
image7 = image7.resize((50,50), Image.ANTIALIAS)
img7 = ImageTk.PhotoImage(image7)
image7 = Label(vent1, image = img7)

image8 = Image.open("frescos.jpg")
image8 = image8.resize((50,50), Image.ANTIALIAS)
img8 = ImageTk.PhotoImage(image8)
image8 = Label(vent1, image = img8)

image9 = Image.open("cafe.jpg")
image9 = image9.resize((50,50), Image.ANTIALIAS)
img9 = ImageTk.PhotoImage(image9)
image9 = Label(vent1, image = img9)

#Se crean las variabes para almacenar las evaluaciones 
radio = IntVar()
radio2 = IntVar()
radio3 = IntVar()

#Se crea la funcion para calcular el monto de la compra y las opciones de cliente
def calcular():

    #Se crean los ciclos para evaluar las elecciones del cliente
    if radio.get()==1:
        plato = "Carne asada"
        precio_1 = 2.50
    elif radio.get()==2:
        plato = "Pollo guisado"
        precio_1 = 2.25
    elif radio.get()==3:
        plato = "Lasaña"
        precio_1 = 3.00
    
    if radio2.get()==1:
        ensalada = "Fresca"
        precio_2 = 0.25
    elif radio2.get()==2:
        ensalada = "Coditos"
        precio_2 = 0.25
    elif radio2.get()==3:
        ensalada = "Rusa"
        precio_2 = 0.25


    if radio3.get()==1:
        bebida ="Gaseosa"
        precio_3= 0.75
    elif radio3.get()==2:
        bebida ="Frescos"
        precio_3= 0.50
    elif radio3.get()==3:
        bebida ="cafe"
        precio_3= 0.65

    #Se imprimen los resultados
    precio_f = precio_1 + precio_2 + precio_3
    print("---------------Factura de los productos---------------")
    print("Plato principal: ",plato, "Precio $: ", precio_1)
    print("Ensalada: ",ensalada,"Precio: $",precio_2 )
    print("Bebida: ",bebida, "Precio: $", precio_3)
    print("Total: $", precio_f)
    print("------------------------------------------------------")


#Se crean los Label
labl1=Label(vent1, bg = "gray",text="Platos.")
labl2=Label(vent1,bg = "gray", text="Ensaladas.")
labl3=Label(vent1,bg = "gray", text="Bebidas.")

#Declaracion de los radio button
rdb1 = Radiobutton(vent1, bg = "gray",text="Carne Asada", value=1, variable=radio)
rdb2 = Radiobutton(vent1, bg = "gray",text="Pollo Guisado", value=2, variable=radio)
rdb3 = Radiobutton(vent1, bg = "gray",text="Lasaña", value=3, variable=radio)

rdb4 = Radiobutton(vent1, bg = "gray",text="Fresca", value=1, variable=radio2)
rdb5 = Radiobutton(vent1, bg = "gray",text="Coditos", value=2, variable=radio2)
rdb6 = Radiobutton(vent1, bg = "gray",text="Rusa", value=3, variable=radio2)

rdb7 = Radiobutton(vent1, bg = "gray",text="Gaseosa", value=1, variable=radio3)
rdb8 = Radiobutton(vent1, bg = "gray",text="Fresco", value=2, variable=radio3)
rdb9 = Radiobutton(vent1, bg = "gray",text="Cafe", value=3, variable=radio3)


#Se crea el boton para imprimir la factura
btn1 = Button(vent1,text="Imprimir factura",command=calcular)

#Se le coloca color a la ventana
vent1.configure(bg='gray')
#Se agrega titulo a la ventana
vent1.title("Cafeteria")

#Se muestran los elementos en pantalla
labl1.place(y=10, x=70, )
labl2.place(y=150, x=70)
image1.place(y=50, x=70)
image2.place(y=50, x=200)
image3.place(y=50, x=350)
image4.place(y=180, x=70)
image5.place(y=180, x=200)
image5.place(y=180, x=200)
image6.place(y=180, x=350)
image7.place(y=310, x=70)
image8.place(y=310, x=200)
image9.place(y=310, x=350)
labl3.place(y=280, x=70)
rdb1.place(y=100, x=50)
rdb2.place(y=100, x=180)
rdb3.place(y=100, x=340)
rdb4.place(y=235, x=50)
rdb5.place(y=235, x=180)
rdb6.place(y=235, x=340)
rdb7.place(y=370, x=50)
rdb8.place(y=370, x=180)
rdb9.place(y=370, x=340)
btn1.place(y=420, x=200)


vent1.mainloop()