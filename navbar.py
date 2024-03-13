import tkinter as tk
from tkinter import PhotoImage, Canvas, NW

# Dictionnaire de couleur
couleur = {"nero": "#252726",
           "purple": "#800080",
           "white": "#FFFFFF"}

# Paramétrage de la fenêtre
app = tk.Tk()
app.title("Mon application")
app.config(bg="gray30")
app.geometry("400x600")
app.iconbitmap("logo.ico")

# Paramétrage Switch
btnEtat = False

#Définir les fonctions switch:
def switch():
    global btnEtat
    if btnEtat is True:
        #Créer une fermeture animée Navbar:
        for x in range(300):
            navLateral.place(x=-x, y=0)
            topFrame.update()
        #Reset couleurs widgets
            bannerTexte.config(fg="purple")
            acceuilText.config(fg=couleur["purple"])
            topFrame.config(bg=couleur["purple"])
            app.config(highlightbackground="gray30")
            btnEtat = False
    else: 
        for x in range(-300, 0):
            navLateral.place(x=x, y=0)
            topFrame.update()
            btnEtat = True

# Chargement image NavBar
navIcon = PhotoImage(file='menu.png')
closeIcon = PhotoImage(file='close.png')
imgFond = PhotoImage(file='back_image3.png')

# Top bar
topFrame = tk.Frame(app, bg=couleur["purple"])
topFrame.pack(side="top", fill=tk.X)

# Texte de top bar
acceuilText = tk.Label(topFrame, text="Python",
                       font="ExtraCondensed 15",
                       bg=couleur["nero"],
                       fg="white", height=2,
                       padx=20)
acceuilText.pack(side="right")

# Image de fond
can = Canvas(app, width=400, height=600)
can.create_image(0, 0, anchor=NW,
                 image=imgFond
                 )
bannerTexte = tk.Label(app, text="DEVELOPPEMENT \n WEB",
                       font="ExtraCondensed 15",
                       fg="purple")

bannerTexte.place(x=100, y=400)
can.pack()

#NavBar Icone
navbarBtn = tk.Button(topFrame, image=navIcon, 
                      bg=couleur["purple"], padx=20, bd=0,
                      activebackground= couleur["purple"], 
                      command=switch)

navbarBtn.place(x=10, y=10)

#NavBar lateral = tk.Frame
navLateral = tk.Frame(app, bg="gray30", width=300, height=600)
navLateral.place(x=-300, y=0)
tk.Label(navLateral, font="ExtraCondensed 15",bg=couleur["purple"],
        fg="black", width=300, height=2, padx=20).place(x=0, y=0)

y= 80

#Les options dans la NavBar Laterale:
option = ["ACCEUIL", "PAGES", "PROFIL",
          "PARAMETRE", "AIDE"]

#Positionnement des options dans la Navbar:
for i in range(5):
    tk.Button(navLateral, text=option[i], font="ExtraCondensed 15",
              bg="gray30", fg=couleur["white"], 
              activebackground="gray30", 
              bd=0).place(x=25, y=y)

    y+=40

#Paramétrage bouton fermeture menu:
fermeBtn = tk.Button(navLateral, image=closeIcon, bg=couleur["purple"],
                     activebackground=couleur["purple"],
                     bd=0, command=switch)
fermeBtn.place(x=250, y=10)


app.mainloop()
