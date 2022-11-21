from logging import root
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from PIL import ImageTk, Image
from tkinter import  Image, Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import Frame
import webbrowser
from cProfile import label
from os import stat
from used.generic2 import leer_imagen
from tkinter import *
from tkinter import ttk

class Liot:
    
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()        
        if(usu == "User" and password == "1234") :
            self.ventana.destroy()
            AppLiot()
        else:
            messagebox.showerror(message="La contraseña o el usuario no son correctos",title="Error")           
                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Inicio de sesión')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,800,500)
        
        logo =utl.leer_imagen("./imagenes/logo.png", (450, 450))
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='white')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='white' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='white')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesión",font=('Open Sans Bold', 30), fg="#EB5066",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Open Sans', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Open Sans', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Open Sans', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Open Sans', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Iniciar sesión",font=('Open Sans', 15,BOLD),bg='#EB5066', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))
        #end frame_form_fill
        self.ventana.mainloop()
        
if __name__ == "__main__":
   Liot()

class AppLiot():
   
    class Ventana(Frame):
        def __init__(self, master, *args):
            super().__init__( master,*args)
            self.menu = True
            self.color = True

            self.frame_inicio = Frame(self.master, bg='white', width=50, height=50)
            self.frame_inicio.grid_propagate(0)
            self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
            self.frame_menu = Frame(self.master, bg='white', width = 50)
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
            #self.imagen_lectura = PhotoImage(file = 'letras.png')
            #Button(self.frame_uno, image= self.imagen_lectura, command= self.pantalla_inicial).place(x=70,y=325)

        def pantalla_reglas(self):
            self.paginas.select([self.frame_dos])
            self.frame_dos.columnconfigure(0, weight=1)
            self.frame_dos.columnconfigure(1, weight=1)
            self.frame_dos.rowconfigure(2, weight=1)
            Button(self.frame_dos ,image= self.ReglaB, command = self.reglaB ,bg='white').place(x=20,y= 10)
            Button(self.frame_dos ,image= self.ReglaC, command = self.reglaC, bg='white',).place(x=320,y= 10)
            Button(self.frame_dos ,image= self.ReglaH, command = self.reglaH, bg='white').place(x=620,y= 10)
            Button(self.frame_dos ,image= self.ReglaJ, command = self.reglaJ, bg='white').place(x=920,y= 10)
            Button(self.frame_dos ,image= self.ReglaS, command = self.reglaS, bg='white').place(x=20,y= 320)
            Button(self.frame_dos ,image= self.ReglaV, command = self.reglaV, bg='white').place(x=320,y= 320)
            Button(self.frame_dos ,image= self.ReglaY, bg='white',command= self.pantalla_reglaY).place(x=620,y= 320)
            Button(self.frame_dos ,image= self.Reglapunt, command = self.reglaPC, bg='white').place(x=920,y= 320)
            #Button(self.frame_dos ,image= self.Reglacoma, bg='white').place(x=660,y= 320)

        def reglaB(self):
            webbrowser.open_new("https://www.canva.com/design/DAFMEynvHyg/ZZ86wNv6te1w9Lquf-8L4g/view?utm_content=DAFMEynvHyg&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu")
##################################################                   
        def reglaC(self):
            webbrowser.open_new("https://www.canva.com/design/DAFMQBWYkMQ/GI0uwiQMhod8ch84rKCVvA/view?utm_content=DAFMQBWYkMQ&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu")
##################################################           
        def reglaV(self):
            webbrowser.open_new("https://www.canva.com/design/DAFMP5tZC7A/dOZLEREy1DWvR-49KVgxZg/view?utm_content=DAFMP5tZC7A&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu")
##################################################               
        def reglaPC(self):
            webbrowser.open_new("https://www.canva.com/design/DAFSCMurjiM/eKUhOuIqG00sBgkGe3usxQ/view?utm_content=DAFSCMurjiM&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu")
##################################################               
        def reglaH(self):
            webbrowser.open_new("https://www.canva.com/design/DAFSB4A7GzE/zrwxk4yzCkSO3Rnmq9Pusw/view?utm_content=DAFSB4A7GzE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
##################################################           
        def reglaS(self):
            webbrowser.open_new("https://www.canva.com/design/DAFMQDCzLjE/8xgM-NWwn2W4JvGpO4mFrg/view?utm_content=DAFMQDCzLjE&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu")
##################################################            
        def reglaY(self):
            webbrowser.open_new("https://www.canva.com/design/DAFSB5wxs0I/93_7_g0_Si2w6VAFb8Lqyg/view?utm_content=DAFSB5wxs0I&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
################################################## 
        def reglaJ(self):
            webbrowser.open_new("https://www.canva.com/design/DAFSEWv_XaA/Hw3mCAYLpcWeLDrNp6yHng/view?utm_content=DAFSEWv_XaA&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu")           
##################################################
        
        def pantalla_Lecturas(self):
            self.paginas.select([self.frame_tres])
            self.frame_tres.columnconfigure(0, weight=1)
            self.frame_tres.columnconfigure(1, weight=1)
            Button(self.frame_tres ,image= self.caperucita, bg='white',command = self.pantalla_lectura).place(x=20,y= 10)
            Button(self.frame_tres ,image= self.lectura2, command = self.tree_pigs, bg='white').place(x=320,y= 10)
            Button(self.frame_tres ,image= self.lectura3, command = self.gatoconbotas, bg='white').place(x=620,y= 10)
            Button(self.frame_tres ,image= self.lectura4, command = self.perroylobo, bg='white').place(x=920,y= 10)
            Button(self.frame_tres ,image= self.lectura5, command = self.risitos, bg='white').place(x=20,y= 320)
            Button(self.frame_tres ,image= self.lectura6, command = self.la_vos, bg='white').place(x=320,y= 320)
            Button(self.frame_tres ,image= self.lectura7, command = self.perro_cazador, bg='white').place(x=620,y= 320)
            Button(self.frame_tres ,image= self.lectura8, command = self.burro_flauta, bg='white').place(x=920,y= 320)
        
        def risitos(self):
            webbrowser.open_new("https://www.canva.com/design/DAFOSG4fL3o/b4sR-0-8SCHX9-43xAjoJg/view?utm_content=DAFOSG4fL3o&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
        
        def tree_pigs(self):
            webbrowser.open_new("https://www.canva.com/design/DAFSE7Cyrms/_c1lYc2z6FsebFYiVV9fnw/view?utm_content=DAFSE7Cyrms&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
        
        def gatoconbotas(self):
            webbrowser.open_new("https://www.guiainfantil.com/articulos/ocio/cuentos-infantiles/el-gato-con-botas-fabulas-para-ninos/")
       
        def la_vos(self):
            webbrowser.open_new("https://gabrielxp123.wixsite.com/comprensionlectora/post/la-mejor-voz")
            
        def perro_cazador(self):
            webbrowser.open_new("https://www.mundoprimaria.com/fabulas-para-ninos/el-viejo-perro-cazador")
            
        def burro_flauta(self):
            webbrowser.open_new("https://www.mundoprimaria.com/fabulas-para-ninos/el-burro-y-la-flauta")
        
        def perroylobo(self):
            webbrowser.open_new("https://www.guiainfantil.com/1358/cuento-infantil-pedro-y-el-lobo.html")




        def open_sitio(self):
            webbrowser.open_new("https://jazmin-jazz.github.io/Liot---Literatura-y-ortograf-a-/")
        
        def open_regla1(self):
            webbrowser.open_new("https://www.canva.com/design/DAFChFmpUjs/N2TXKAtjcCw8VKbMNw64Ww/view?utm_content=DAFChFmpUjs&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")
        
        def open_manual(self):
            webbrowser.open_new("https://issuu.com/carlos.giron2023/docs/manual_de_usuario")
            
        def open_lectura1(self):
            webbrowser.open_new("https://www.canva.com/design/DAFNV7jERD0/Gh7hCkDQCksRGwbCgZvb-w/view?utm_content=DAFNV7jERD0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")

        def pantalla_Quizzes(self):
            self.paginas.select([self.frame_cuatro])	
            self.frame_cuatro.columnconfigure(0, weight=1)
            self.frame_cuatro.columnconfigure(1, weight=1)
            Button(self.frame_cuatro ,image= self.QuizzB, command = self.quizz_de_B,bg='white').place(x=20,y= 10)
            Button(self.frame_cuatro ,image= self.QuizzC, command = self.quizz_de_C, bg='white').place(x=320,y= 10)
            Button(self.frame_cuatro ,image= self.QuizzH, command = self.quizz_de_H, bg='white').place(x=620,y= 10)
            Button(self.frame_cuatro ,image= self.QuizzJ, command = self.quizz_de_J, bg='white').place(x=920,y= 10)
            Button(self.frame_cuatro ,image= self.QuizzS, command = self.quizz_de_S, bg='white').place(x=20,y= 320)
            Button(self.frame_cuatro ,image= self.QuizzV, command = self.quizz_de_V, bg='white').place(x=320,y= 320)
            Button(self.frame_cuatro ,image= self.QuizzY, command = self.quizz_de_Y, bg='white').place(x=620,y= 320)
            Button(self.frame_cuatro ,image= self.QuizzCom, command = self.quizz_de_Puntoycoma, bg='white').place(x=920,y= 320)
               
#DONE#############################################################################################
        def quizz_de_B(self):
            webbrowser.open_new("https://forms.office.com/Pages/ResponsePage.aspx?id=RL3j2LoLa0KVLa2nuxc5PNVYNA_X4ohOjOWO2uRyZchUMFRMVVBXSDdIS1pYRjNGVTVTWDVFTzNDNy4u")
###DONE###############################################################################################
        def quizz_de_H(self):
            webbrowser.open_new("https://forms.office.com/Pages/ResponsePage.aspx?id=RL3j2LoLa0KVLa2nuxc5PNVYNA_X4ohOjOWO2uRyZchUREhSMzVRWVo4N0RVWDVJUzhETjRHTFM5RS4u")
####DONE##############################################################################################
        def quizz_de_C(self):
            webbrowser.open_new("https://forms.office.com/r/1GyZWYX6pZ")
###DONE###############################################################################################            
        def quizz_de_J(self):
            webbrowser.open_new("https://forms.office.com/r/ADDan7emz9")
###DONE###############################################################################################
        def quizz_de_S(self):
            webbrowser.open_new("https://forms.office.com/r/1GyZWYX6pZ")
####DONE##############################################################################################
        def quizz_de_V(self):
            webbrowser.open_new("https://forms.office.com/r/7exV5dx7nW")
##################################################################################################         
        def quizz_de_Y(self):
            webbrowser.open_new("https://forms.office.com/r/PwnbyDvvRy")
########done##########################################################################################
        def quizz_de_Puntoycoma(self):
            webbrowser.open_new("https://forms.office.com/r/M3YCN3PYbi")
##################################################################################################
            
        def pantalla_sitio(self):
            self.paginas.select([self.frame_cinco])
            self.frame_cinco.columnconfigure(0, weight=1)
            self.frame_cinco.columnconfigure(1, weight=1)
            self.frame_cinco.columnconfigure(2, weight=1)
            self.frame_cinco.rowconfigure(2, weight=1)
            Label(self.frame_cinco ,image= self.fondo, bg='white').place(x=0,y= 0)
            Label(self.frame_cinco ,image= self.nota, bg='white').place(x=200,y= 0)
            Label(self.frame_cinco ,image= self.logo3, bg='white').place(x=40,y=115)
            Label(self.frame_cinco ,image= self.nota3, bg='white').place(x=600,y=115)
            buttonIr=Button(self.frame_cinco, image= self.botonIr, bd=0, bg = "white", command= self.open_sitio)
            buttonIr.place(x=800, y=460)
############################################################################################################################
        def pantalla_reglaY(self):
            self.paginas.select([self.frame_seis])

            next1 = leer_imagen("./img carrusel/next.png",(60,60))
            privius = leer_imagen("./img carrusel/previous.png",(60,60))
            regla_2 = leer_imagen("./Reglas/reglaY1.png",(1100,620))
            regla_3 = leer_imagen("./Reglas/reglaY2.png",(1100,620))
            regla_4 = leer_imagen("./Reglas/reglaY3.png",(1100,620))
            regla_5 = leer_imagen("./Reglas/reglaY4.png",(1100,620))
            regla_6 = leer_imagen("./Reglas/reglaY5.png",(1100,620))
            regla_7 = leer_imagen("./Reglas/reglaY6.png",(1100,620))
            regla_8 = leer_imagen("./Reglas/reglaY7.png",(1100,620))
            regla_9 = leer_imagen("./Reglas/reglaY8.png",(1100,620))
            regla_10 = leer_imagen("./Reglas/reglaY9.png",(1100,620))
            regla_11 = leer_imagen("./Reglas/reglaY10.png",(1100,620))
            regla_12 = leer_imagen("./Reglas/reglaY11.png",(1100,620))

            lista_cuadros = [regla_2, regla_3, regla_4, regla_5, regla_6, regla_7, regla_8, regla_9, regla_10, regla_11, regla_12]

            def adelante(num_imagen):
                global label_pre
                global btn_adelante
                global btn_atras

                label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="white")
                label_pre.place_forget()
                 
                btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
                btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
                if num_imagen == 10:
                    btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",state=DISABLED)

                label_pre.place(x=10,y=55)
                btn_atras.place(x=50,y=400)
                btn_adelante.place(x=1215,y=400)

            def atras(num_imagen):
                global label_pre
                global btn_adelante
                global btn_atras

                label_pre.place_forget()
                label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="white")

                btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
                btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
                if num_imagen == 0:
                    btn_atras = Button(frame_central,image=privius, bg="white",bd=0,activebackground="white",state=DISABLED)

                label_pre.place(x=10,y=55)
                btn_atras.place(x=50,y= 400)
                btn_adelante.place(x=1215,y=400)


            frame_central = Frame(self.frame_seis, height= 900, width=1355, bg="white")
            frame_central.place(x=-60,y=-155)

            btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", state=DISABLED)
            btn_atras.place(x=50,y= 400)
            btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(1))
            btn_adelante.place(x= 1215,y= 400)

            frame1 = Frame(frame_central, height=900, width=1120, bg="white")
            frame1.place(x=100,y=90)
            label_pre = Label(frame1,image= regla_2, bg="white")
            label_pre.place(x=10,y=55)


###########################################################################      
        def pantalla_ayuda2(self):
            self.paginas.select([self.frame_siete])
            self.frame_siete.columnconfigure(0, weight=1)
            self.frame_siete.columnconfigure(1, weight=1)
            self.frame_siete.columnconfigure(2, weight=1)
            self.frame_siete.rowconfigure(2, weight=1)
            Button(self.frame_siete ,image= self.manual1, bg='white', command=self.open_manual).place(x=60,y=10)
            Label(self.frame_siete ,text= "Manual de usuario", bg= 'white',font= ('Lucida Sans', 15)).place(x=95,y=270)
            Button(self.frame_siete ,image= self.manual2, bg='white', command=self.open_manual).place(x=360,y=10)
            Label(self.frame_siete ,text= "Manual técnico", bg= 'white',font= ('Lucida Sans', 15)).place(x=396,y=270)

################################################################################################
 
        def pantalla_lectura(self):
            self.paginas.select([self.frame_ocho])

            next1 = leer_imagen("./img carrusel/next.png",(60,60))
            privius = leer_imagen("./img carrusel/previous.png",(60,60))
            foto_grup1 = leer_imagen("./img carrusel/img1.png",(1100,620))
            img_2 = leer_imagen("./img carrusel/img2.png",(1100,620))
            img_3 = leer_imagen("./img carrusel/img3.png",(1100,620))
            img_4 = leer_imagen("./img carrusel/img4.png",(1100,620))
            img_5 = leer_imagen("./img carrusel/img5.png",(1100,620))
            img_6 = leer_imagen("./img carrusel/img6.png",(1100,620))
            img_7 = leer_imagen("./img carrusel/img7.png",(1100,620))

            lista_cuadros = [foto_grup1, img_2, img_3, img_4, img_5, img_6, img_7]

            def adelante(num_imagen):
                global label_pre
                global btn_adelante
                global btn_atras

                label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="white")
                label_pre.place_forget()
                 
                btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
                btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
                if num_imagen == 6:
                    btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",state=DISABLED)

                label_pre.place(x=10,y=55)
                btn_atras.place(x=50,y=400)
                btn_adelante.place(x=1215,y=400)

            def atras(num_imagen):
                global label_pre
                global btn_adelante
                global btn_atras

                label_pre.place_forget()
                label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="white")

                btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
                btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
                if num_imagen == 0:
                    btn_atras = Button(frame_central,image=privius, bg="white",bd=0,activebackground="white",state=DISABLED)

                label_pre.place(x=10,y=55)
                btn_atras.place(x=50,y= 400)
                btn_adelante.place(x=1215,y=400)

            frame_central = Frame(self.frame_ocho, height= 900, width=1355, bg="white")
            frame_central.place(x=-60,y=-155)

            btn_atras = Button(frame_central,image=privius,bg="white",bd=0,activebackground="white", state=DISABLED)
            btn_atras.place(x=50,y= 400)
            btn_adelante = Button(frame_central,image=next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(1))
            btn_adelante.place(x= 1215,y= 400)

            frame1 = Frame(frame_central, height=900, width=1120, bg="white")
            frame1.place(x=100,y=90)
            label_pre = Label(frame1,image=foto_grup1, bg="white")
            label_pre.place(x=10,y=55)

###################################################################################

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
                    if clik_inicio is None:
                        self.frame_menu.grid_propagate(0)		
                        self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
                        self.bt_cerrar.grid_propagate(0)
                        self.bt_cerrar.config(width=i)
                        self.pantalla_inicial()
                self.menu = True


        def widgets(self):
            self.imagen_inicio = PhotoImage(file ='inicio.png')
            self.imagen_menu = PhotoImage(file ='menu.png')
            self.imagen_cuenta = PhotoImage(file ='letras2.png')
            self.imagen_sitio = PhotoImage(file ='lecturas.png')
            self.imagen_config = PhotoImage(file ='quizz2.png')
            self.imagen_ayuda = PhotoImage(file ='sitio.png')
            self.imagen_ajustes = PhotoImage(file ='ayuda2.png')
            self.imagen_ayuda2 = PhotoImage(file ='ayuda2.png')
            #self.imagen_lectura = PhotoImage(file = 'letras.png')
            ###################################################################
            self.ReglaY = PhotoImage (file='uso y.png')
            self.ReglaB = PhotoImage (file='uso b.png')
            self.ReglaC = PhotoImage (file='uso c.png')
            self.ReglaH = PhotoImage (file='uso h.png')
            self.ReglaS = PhotoImage (file='uso s.png')
            self.ReglaV = PhotoImage (file='uso v.png')
            self.ReglaJ = PhotoImage (file='uso j.png')
            self.Reglapunt = PhotoImage (file='uso punco.png')
            #################################################################
            self.caperucita = PhotoImage (file='./img cuentos/caperucita.png')
            self.lectura2 = PhotoImage (file='./img cuentos/cerditos.png')
            self.lectura3 = PhotoImage (file='./img cuentos/gato.png')
            self.lectura4 = PhotoImage (file='./img cuentos/lobo.png')
            self.lectura5 = PhotoImage (file='./img cuentos/risitos.png')
            self.lectura6 = PhotoImage (file='./img cuentos/voz.png')
            self.lectura7 = PhotoImage (file='./img cuentos/perro.png')
            self.lectura8 = PhotoImage (file='./img cuentos/burro.png')
            #################################################################
            self.logo = PhotoImage(file ='portada.png')
            self.fondo = PhotoImage(file ='fondo.png')
            self.nota = PhotoImage(file ='nota.png')
            self.nota3 = PhotoImage(file ='nota3.png')
            self.logo3 = PhotoImage(file ='logo3.png')
            self.botonIr = PhotoImage(file ='ir.png')
            self.manual1 = PhotoImage(file ='manual1.png')
            self.manual2 = PhotoImage(file ='manual2.png')
            ##################################################################
            self.QuizzH = PhotoImage (file='quizz h.png')
            self.QuizzB = PhotoImage (file='quizz b.png')
            self.QuizzC = PhotoImage (file='quizz c.png')
            self.QuizzY = PhotoImage (file='Quizz Y.png')
            self.QuizzS = PhotoImage (file='quizz s.png')
            self.QuizzJ = PhotoImage (file='quizz j.png')
            self.QuizzV = PhotoImage (file='quizz v.png')
            self.QuizzCom = PhotoImage (file='quizz com.png')
            ##################################################################
            self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='white',activebackground='white', bd=0, command = self.menu_lateral)
            self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
            self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='white',activebackground='white', bd=0, command = self.menu_lateral)
            self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)	

            #BOTONES Y ETIQUETAS DEL MENU LATERAL 
            #Items y texto con fondo gris #ecf0f1
            Button(self.frame_menu, image= self.imagen_cuenta, bg='white', activebackground='white', bd=0, command = self.pantalla_reglas).grid(column=0, row=1, pady=20,padx=10)
            Button(self.frame_menu, image= self.imagen_sitio, bg='white',activebackground='white', bd=0, command = self.pantalla_Lecturas).grid(column=0, row=2, pady=20,padx=10)
            Button(self.frame_menu, image= self.imagen_config, bg= 'white',activebackground='white', bd=0, command = self.pantalla_Quizzes).grid(column=0, row=3, pady=20,padx=10)
            Button(self.frame_menu, image= self.imagen_ayuda, bg= 'white',activebackground='white', bd=0, command = self.pantalla_sitio).grid(column=0, row=4, pady=20,padx=10)		
            #Button(self.frame_menu, image= self.imagen_ajustes, bg= '#ecf0f1',activebackground='#ecf0f1', bd=0, command = self.pantalla_reglaY).grid(column=0, row=5, pady=20,padx=10)
            Button(self.frame_menu, image= self.imagen_ayuda2, bg= 'white',activebackground='white', bd=0, command = self.pantalla_ayuda2).grid(column=0, row=5, pady=20,padx=10)

            Label(self.frame_menu, text= 'Reglas', bg= 'white', fg= '#666a88', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
            Label(self.frame_menu, text= 'Lecturas', bg= 'white', fg= '#666a88', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
            Label(self.frame_menu, text= 'Quizzes', bg= 'white', fg= '#666a88', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
            Label(self.frame_menu, text= 'Sitio web', bg= 'white', fg= '#666a88', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)	
            Label(self.frame_menu, text= 'Ayuda', bg= 'white', fg= '#666a88', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)
            #Label(self.frame_menu, text= '', bg= '#ecf0f1', fg= '#666a88', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=5, pady=20, padx=2)

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
            self.frame_siete = Frame(self.paginas, bg='white')
            self.frame_ocho = Frame(self.paginas, bg='white')
            self.frame_quizz_h = Frame(self.paginas, bg='white')
            self.paginas.add(self.frame_uno)
            self.paginas.add(self.frame_dos)
            self.paginas.add(self.frame_tres)
            self.paginas.add(self.frame_cuatro)
            self.paginas.add(self.frame_cinco)
            self.paginas.add(self.frame_seis)
            self.paginas.add(self.frame_siete)
            self.paginas.add(self.frame_ocho)
            self.paginas.add(self.frame_quizz_h)

            ######################## FRAME TITULO #################
            #self.titulo = Label(self.frame_top,text= 'APLICACION DE ESCRITORIO EN PYTHON CON TKINTER', bg='white', fg= 'DarkOrchid1', font= ('Imprint MT Shadow', 15, 'bold'))
            #self.titulo.pack(expand=1)
            ######################## VENTANA PRINCIPAL #################
            #Label(self.frame_uno, text= 'Electrónica Programación y Tecnología', bg='DarkOrchid1', fg= 'white', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
            Label(self.frame_uno ,image= self.logo, bg='white').place(x=0,y=-10)#.pack(expand=1)

################################################################################
    if __name__ == "__main__":
        ventana = Tk()
        ventana.title('Liot')
        ventana.minsize(height= 650, width=1200)
        ventana.geometry('1000x500+180+80')
        ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='lecturas.png'))	
        app = Ventana(ventana)
        app.mainloop()