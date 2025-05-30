import tkinter as tk 

class Suma:
  def aru(self):
        self.a=entrada2.get
        self.b=entrada2.get

  def operacion(self):
     return self.a + self.b
     
    



ventana=tk.Tk()
ventana.title("Suma con clases")
ventana.geometry("450x300")

etiqueta=tk.Label(ventana, text="Ingrese el primer numero")
etiqueta.pack
entrada=tk.Entry(ventana)
entrada.pack
etiqueta2=tk.Label(ventana, text="Ingrese el segundo numero")
etiqueta2.pack
entrada2=tk.Entry(ventana)
entrada2.pack

boton=tk.Button(ventana,text="sumar",command=Suma)
boton.pack
yes=Suma()
yes.aru()
resultado=yes.operacion()
eti_resultado=tk.Label(text=f"El resultado es{resultado}")
eti_resultado.pack()


ventana.mainloop()