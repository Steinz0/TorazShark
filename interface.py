from tkinter.constants import END, SUNKEN, WORD
from tkinter import Label, Menu, Frame, StringVar, YES, Tk, Button
from tkinter import filedialog
import tkinter.scrolledtext as ScrolledText

from trame import trace_to_trames
from analyzer import answer

listTrames = []

def browseFiles():
    path = filedialog.askopenfilename(initialdir="/",
                                      title="Select a File",
                                      filetypes=(("Text files",
                                                  "*.txt*"),
                                                 ("all files",
                                                  "*.*")))
    
    for t in trace_to_trames(path):
        listTrames.append(t)

    # Reinitialise les differents champs de l'interface et variables
    
    for child in frameNbTrames.winfo_children():
        child.destroy()

    #Creer les boutons 
    createButtonTrame()


# Permet d'afficher la trame et le resultat de l'analyse
def loadTrame(trame):
    s = ''
    nb = 1
    print(trame)
    res.set(answer(trame)) # Contient l'analyse de la trame

    scrollRes.delete(1.0,END)
    scrollRes.insert('insert', res.get())
    
    # creer un str (s) de la trame sur le format suivant : 16 octets par lignes
    for octet in trame:
        if not nb % 16:
            s += '\n'
        s += ' ' + octet
        nb += 1

    stringTrame.set(s[1:]) # Enleve le premier espace
    
    scrollTrame.delete(1.0,END)
    scrollTrame.insert('insert', stringTrame.get())
    


# Permet de creer n boutons (n nombre de trames)
def createButtonTrame():
    for i in range(len(listTrames)):
        s = "trame " + str(i)
        button = Button(frameNbTrames, text=s, command= lambda k=i:loadTrame(listTrames[k]), padx=5, pady=5, activebackground='#53597e') # Action du bouton : lance loadTrame avec la trame concernee (liste des octets)
        button.pack(pady=5)


# creation de la fenetre
app = Tk()


res = StringVar()
stringTrame = StringVar()

# Redimmensionne la fenetre de tel sorte quelle fasse 800x600 et est centree au milieu de l'ecran
screenX = int(app.winfo_screenwidth())
screenY = int(app.winfo_screenheight())
windowX = 800
windowY = 800
posX = screenX//2 - windowX//2
posY = screenY//2 - windowY//2
geo = "{}x{}+{}+{}".format(windowX,windowY,posX,posY)
app.geometry(geo)

app.config(background='#5267f0')

# Frame (Boite) ou va contenir les boutons pour les trames 
frameNbTrames = Frame(app, bg='#f04711', bd=1, relief=SUNKEN)
frameNbTrames.pack(expand=YES)

# Frame (Boite) ou va contenir la trame
frameTrame = Frame(app, bg='#5267f0', bd=1, relief=SUNKEN)
frameTrame.pack(expand=YES)


# Frame (Boite) ou va contenir l'analyse de la trame
frameRes = Frame(app, bg='#5267f0', bd=1, relief=SUNKEN)
frameRes.pack(expand=YES)
#labelRes = Label(frameRes, textvariable=res, anchor='nw', justify='left')  # Insertion de la trame via un Message dans l'interface
#labelRes.pack()

# Creation du menu
fileMenu = Menu(app)

# Creation du sous menu
subMenu = Menu(fileMenu, tearoff=0)

# Ajout de new et quit
subMenu.add_command(label="New", command=browseFiles)   #Action : lance l'explorateur et le client doit selectionner sa trame
subMenu.add_command(label="Quit", command=app.quit)     #Action : quitte l'appli
subMenu.add_command(label="Size", command=print(str(app.winfo_width)))
# Met subMenu dans fileMenu
fileMenu.add_cascade(label="File", menu=subMenu)

# Definit fileMenu comme le menu de l'app
app.configure(menu=fileMenu)


scrollTrame = ScrolledText.ScrolledText(frameTrame, wrap=WORD)
scrollTrame.pack()

scrollTrame.insert('insert',stringTrame.get())

scrollRes = ScrolledText.ScrolledText(frameRes, wrap=WORD)
scrollRes.pack()

scrollRes.insert('insert',res.get())

# lancement de la fenetre
app.mainloop()