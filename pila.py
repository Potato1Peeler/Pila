import matplotlib.pyplot as plt

class Pila:
    def __init__(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
        print(f"Apilado: {item} - Pila actual: {self.items}")
        self.graficar()
    
    def desapilar(self):
        if not self.esta_vacia():
            item = self.items.pop()
            print(f"Desapilado: {item} - Pila actual: {self.items}")
        else:
            print("La pila está vacía, no se puede desapilar.")
        self.graficar()
    
    def graficar(self):
        plt.clf()  
        plt.bar(range(len(self.items)), self.items, color='blue')
        plt.xlabel('Índice')
        plt.ylabel('Valor')
        plt.title('Estado actual de la pila')
        plt.pause(0.5) 

def main():
    pila = Pila()
    plt.ion()  
    
  
    pila.apilar(5)
    pila.apilar(10)
    pila.apilar(15)
    pila.desapilar()
    pila.apilar(20)
    pila.desapilar()
    pila.desapilar()
    pila.desapilar()

    plt.ioff()  
    plt.show()  

if __name__ == "__main__":
    main()
