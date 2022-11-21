from tkinter import  Image, Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import Frame

class Ventana(Frame):
	def __init__(self, master, *args):
		super().__init__( master,*args)
		self.menu = True
		self.color = True

		self.frame_inicio = Frame(self.master, bg='white', width=50, height=50)
		self.frame_inicio.grid_propagate(0)
		self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
		self.frame_menu = Frame(self.master, bg='#ecf0f1', width = 50)
		self.frame_menu.grid_propagate(0)
		self.frame_menu.grid(column=0, row = 1, sticky='nsew')
		self.frame_principal = Frame(self.master, bg='white')
		self.frame_principal.grid(column=1, row=1, sticky='nsew')
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.rowconfigure(0, weight=1)
		self.widgets()		

	def pantalla_inicial(self):
		self.paginas.select([self.frame_uno])
		self.imagen_lectura = PhotoImage(file = 'letras.png')
		Button(self.frame_uno, image= self.imagen_lectura, command= self.pantalla_inicial).place(x=70,y=325)

	def pantalla_cuenta(self):
		self.paginas.select([self.frame_dos])
		self.frame_dos.columnconfigure(0, weight=1)
		self.frame_dos.columnconfigure(1, weight=1)
		self.frame_dos.rowconfigure(2, weight=1)


	def pantalla_sitio(self):
		self.paginas.select([self.frame_tres])
		self.frame_tres.columnconfigure(0, weight=1)
		self.frame_tres.columnconfigure(1, weight=1)

	def pantalla_config(self):
		self.paginas.select([self.frame_cuatro])	
		self.frame_cuatro.columnconfigure(0, weight=1)
		self.frame_cuatro.columnconfigure(1, weight=1)

	def pantalla_ayuda(self):
		self.paginas.select([self.frame_cinco])
		self.frame_cinco.columnconfigure(0, weight=1)
		self.frame_cinco.columnconfigure(1, weight=1)
		self.frame_cinco.columnconfigure(2, weight=1)
		self.frame_cinco.rowconfigure(2, weight=1)


	def pantalla_ajustes(self):
		self.paginas.select([self.frame_seis])

	def menu_lateral(self):
		if self.menu is True:
			for i in range(50,170,10):				
				self.frame_menu.config(width= i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_cerrar.grid_forget()
				if clik_inicio is None:		
					self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
					self.bt_inicio.grid_propagate(0)
					self.bt_inicio.config(width=i)
					self.pantalla_inicial()
			self.menu = False
		else:
			for i in range(170,50,-10):
				self.frame_menu.config(width=  i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_inicio.grid_forget()
				if clik_inicio is   None:
					self.frame_menu.grid_propagate(0)		
					self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
					self.bt_cerrar.grid_propagate(0)
					self.bt_cerrar.config(width=i)
					self.pantalla_inicial()
			self.menu = True


	def widgets(self):
		self.imagen_inicio = PhotoImage(file ='inicio.png')
		self.imagen_menu = PhotoImage(file ='menu.png')
		self.imagen_cuenta = PhotoImage(file ='usuario.png')
		self.imagen_sitio = PhotoImage(file ='sitio.png')
		self.imagen_config = PhotoImage(file ='config.png')
		self.imagen_ayuda = PhotoImage(file ='ayuda.png')
		self.imagen_ajustes = PhotoImage(file ='ajustes.png')
		#self.imagen_lectura = PhotoImage(file = 'letras.png')

		self.logo = PhotoImage(file ='portada.png')

		self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='#ecf0f1',activebackground='#ecf0f1', bd=0, command = self.menu_lateral)
		self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
		self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='#ecf0f1',activebackground='#ecf0f1', bd=0, command = self.menu_lateral)
		self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)	
		#BOTONES Y ETIQUETAS DEL MENU LATERAL 
		Button(self.frame_menu, image= self.imagen_cuenta, bg='#ecf0f1', activebackground='#ecf0f1', bd=0, command = self.pantalla_cuenta).grid(column=0, row=1, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_sitio, bg='#ecf0f1',activebackground='#ecf0f1', bd=0, command =self.pantalla_sitio ).grid(column=0, row=2, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_config, bg= '#ecf0f1',activebackground='#ecf0f1', bd=0, command = self.pantalla_config).grid(column=0, row=3, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_ayuda, bg= '#ecf0f1',activebackground='#ecf0f1', bd=0, command = self.pantalla_ayuda).grid(column=0, row=4, pady=20,padx=10)		
		Button(self.frame_menu, image= self.imagen_ajustes, bg= '#ecf0f1',activebackground='#ecf0f1', bd=0, command = self.pantalla_ajustes).grid(column=0, row=5, pady=20,padx=10)

		Label(self.frame_menu, text= 'Mi cuenta', bg= '#ecf0f1', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
		Label(self.frame_menu, text= 'Sitio web', bg= '#ecf0f1', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
		Label(self.frame_menu, text= 'Ajustes', bg= '#ecf0f1', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
		Label(self.frame_menu, text= 'Ayuda', bg= '#ecf0f1', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)	
		Label(self.frame_menu, text= 'Ajustes', bg= '#ecf0f1', fg= 'DarkOrchid1', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)

        	#############################  CREAR  PÁGINAS  ##############################
		estilo_paginas = ttk.Style()
		estilo_paginas.configure("TNotebook", background='white', foreground='white', padding=0, borderwidth=0)
		estilo_paginas.theme_use('default')
		estilo_paginas.configure("TNotebook", background='white', borderwidth=0)
		estilo_paginas.configure("TNotebook.Tab", background="white", borderwidth=0)
		estilo_paginas.map("TNotebook", background=[("selected", 'white')])
		estilo_paginas.map("TNotebook.Tab", background=[("selected", 'white')], foreground=[("selected", 'white')]);

		#CREACCION DE LAS PAGINAS 
		self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
		self.paginas.grid(column=0,row=0, sticky='nsew')
		self.frame_uno = Frame(self.paginas, bg='white')
		self.frame_dos = Frame(self.paginas, bg='white')
		self.frame_tres = Frame(self.paginas, bg='white')
		self.frame_cuatro = Frame(self.paginas, bg='white')
		self.frame_cinco = Frame(self.paginas, bg='white')
		self.frame_seis = Frame(self.paginas, bg='white')
		self.paginas.add(self.frame_uno)
		self.paginas.add(self.frame_dos)
		self.paginas.add(self.frame_tres)
		self.paginas.add(self.frame_cuatro)
		self.paginas.add(self.frame_cinco)
		self.paginas.add(self.frame_seis)

		######################## FRAME TITULO #################
		#self.titulo = Label(self.frame_top,text= 'APLICACION DE ESCRITORIO EN PYTHON CON TKINTER', bg='white', fg= 'DarkOrchid1', font= ('Imprint MT Shadow', 15, 'bold'))
		#self.titulo.pack(expand=1)
		######################## VENTANA PRINCIPAL #################
		#Label(self.frame_uno, text= 'Electrónica Programación y Tecnología', bg='DarkOrchid1', fg= 'white', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
		Label(self.frame_uno ,image= self.logo, bg='white').place(x=0,y=-10)#.pack(expand=1)



if __name__ == "__main__":
	ventana = Tk()
	ventana.title('Liot')
	ventana.minsize(height= 475, width=795)
	ventana.geometry('1000x500+180+80')
	ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))	
	app = Ventana(ventana)
	app.mainloop()
