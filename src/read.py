
import tkinter as tk
import tkinter.simpledialog

class Read():
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

    def ejecutar(self, ts):
        path = tk.Tk()
        path.geometry('200x200')
        path.title('read.')

        entrada = tk.simpledialog.askstring("title", "Ingrese texto")
        path.mainloop()        
        return entrada