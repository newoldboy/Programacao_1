import tkinter as tk
from platform import python_version

def teste(self):   
	return 1
def main(args):
	root = tk.Tk(className='Python')
	root.geometry("1000x600+90+90") 

	l1= tk.Label(root, text="Programa para Urna", bg="red", fg="white").grid(row=0,column=0)
	l2= tk.Label(root, text="Texto intermediário", bg="yellow", fg="black").grid(row=0,column=1)
	l3= tk.Label(root, text="Texto inferior", bg="green", fg="white").grid(row=0,column=2)
        
	lblC= tk.Label(root, text="Graus Centígrados").grid(row=3,column=1) 

	btnCalculaC = tk.Button(root,text=u"Porra",command=teste).grid(row=3,column=2) 
    # self.btnCalculaC.grid(column=2,row=3)          
	
     
	root.mainloop()
	return 0

if __name__ == '__main__':
	print (python_version())  
	import sys
	sys.exit(main(sys.argv))