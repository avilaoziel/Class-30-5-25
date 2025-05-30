class Suma:
    def aru(self):
     self.a=float(input("ingrese el primer numero\n"))
     self.b=float(input("ingrese el otro numero\n"))

    def operacion(self):
       return self.a + self.b
    




yes=Suma()
yes.aru()
resultado=yes.operacion()
print(resultado)
       