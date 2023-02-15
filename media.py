class Media:
    ArrayNotas=[]

    def notas(self):
       return self.ArrayNotas
    
    def add(self, number):
        if(number<0 or number >10):
            raise ValueError
        self.ArrayNotas.append(number)
    
    def media(self):
        suma=0
        for a in self.ArrayNotas:
            suma= suma+a
        return suma/len(self.ArrayNotas)
