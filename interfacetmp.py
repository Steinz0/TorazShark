from Tcp import window
from tkinter import Menu, Frame, Scrollbar, YES, Tk, Label, Button, Message
from tkinter import filedialog

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
    
    tempLst = trace_to_trames(path)

    # Reinitialise les differents champs de l'interface et variables
    listTrames.clear()
    for child in frameNbTrames.winfo_children():
        child.destroy()
    for child in frameTrame.winfo_children():
        child.destroy()
    for child in frameRes.winfo_children():
        child.destroy()

    #MAJ de la liste de trames
    for lst in tempLst:
        listTrames.append(lst)

    #Creer les boutons 
    createButtonTrame()


# Permet d'afficher la trame et le resultat de l'analyse
def loadTrame(trame):
    s = ''
    nb = 0
    res = answer(trame) # Contient l'analyse de la trame
    
    # creer un str (s) de la trame sur le format suivant : 16 octets par lignes
    for octet in trame:
        if nb % 16:
            s += '\n'
        s += ' ' + octet
    s = s[1:] # Enleve le premier espace

    # Enleve toutes les potentielles trames et analyse qu'ils pouvaient y avoir avant dans l'interface
    for child in frameNbTrames.winfo_children():
        child.destroy()

        
    msgTrame.configure(text=s)  # Insertion de la trame via un Message dans l'interface

    resTrame.configure(text=res)  # Insertion de l'analyse de la trame via un Message dans l'interface


# Permet de creer n boutons (n nombre de trames)
def createButtonTrame():
    print()
    for i in range(len(listTrames)):
        s = "trame " + str(i)
        button = Button(frameNbTrames, text=s, command= lambda k=i:loadTrame(listTrames[k])) # Action du bouton : lance loadTrame avec la trame concernee (liste des octets)
        button.pack()


# creation de la fenetre
app = Tk()

# Redimmensionne la fenetre de tel sorte quelle fasse 800x600 et est centree au milieu de l'ecran
screenX = int(app.winfo_screenwidth())
screenY = int(app.winfo_screenheight())
windowX = 800
windowY = 600
posX = screenX//2 - windowX//2
posY = screenY//2 - windowY//2
geo = "{}x{}+{}+{}".format(windowX,windowY,posX,posY)
app.geometry(geo)

# Frame (Boite) ou va contenir les boutons pour les trames 
frameNbTrames = Frame(app)
frameNbTrames.pack(expand=YES)

# Frame (Boite) ou va contenir la trame
frameTrame = Frame(app)
frameTrame.pack(expand=YES)

msgTrame = Message(frameTrame)

# Frame (Boite) ou va contenir l'analyse de la trame
frameRes = Frame(app)
frameRes.pack(expand=YES)

resTrame = Message(frameRes)

# Creation du menu
fileMenu = Menu(app)

# Creation du sous menu
subMenu = Menu(fileMenu, tearoff=0)

# Ajout de new et quit
subMenu.add_command(label="New", command=browseFiles)   #Action : lance l'explorateur et le client doit selectionner sa trame
subMenu.add_command(label="Quit", command=app.quit)     #Action : quitte l'appli

# Met subMenu dans fileMenu
fileMenu.add_cascade(label="File", menu=subMenu)

# Creation de scrollbar pour les frames frameTrame et frameRes
scrollbarTrame = Scrollbar(frameTrame)

# Definit fileMenu comme le menu de l'app
app.configure(menu=fileMenu)

# lancement de la fenetre
app.mainloop()