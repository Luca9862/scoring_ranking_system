import wikipediaapi
import tkinter

wiki = wikipediaapi.Wikipedia('it')

persone = [
    'Romolo',
    'Gaio Giulio Cesare',
    'Dante Alighieri',
    'Leonardo Da Vinci',
    'Benito Mussolini',
    'Umberto II di Savoia',
    'Rita Levi-Montalcini',
    'Silvio Berlusconi',
    'Mario Draghi'
    ]

pesi = {
    'pagine': 0.001,
    'lingue': 0.002,
    'bibliografie': 0.002,
    'categorie': 0.002,
    'sezioni' : 0.001,
    'parole': 0.001
}
#Funzione che restituisce il numero di pagine di Wikipedia relative a quella persona
def num_pagine(persona):
    page = wiki.page(persona)
    if page.exists():
        return 1
    else:
        return 0
    
#Funzione che restituisce il numero di lingue in cui è disponibile la pagina Wikipedia di una data persona
def num_lingue(persona):
    page = wiki.page(persona)
    if page.exists():
        return len(page.langlinks.keys())
    else:
        return 0
    
#Funzione che restituisce il numero di bibliografia presenti nella pagina Wikipedia di una data persona
def num_bibliografie(persona):
    page = wiki.page(persona)
    if page.exists():
        sections = page.sections
        for section in sections:
            if section.title == 'Bibliografia':
                text = section.text
                lines = text.split('\n')
                return len(lines)
    return 0

#Funzione che restituisce il numero di categorie presenti nella pagina Wikipedia di una data persona
def num_categorie(persona):
    page = wiki.page(persona)
    if page.exists():
        return len(page.categories)
    else:
        return 0
    
#Funzione che restituisce il numero di sezioni presenti nella pagina Wikipedia di una data persona
def num_sezioni(persona):
    page = wiki.page(persona)
    if page.exists():
        return len(page.sections)
    else:
        return 0
    
#Funzione che restituisce il numero di parole presenti nella pagina Wikipedia di una data persona
def num_parole(persona):
    page = wiki.page(persona)
    if page.exists():
        text = page.text
        words = text.split()
        return len(words)
    else:
        return 0
    
def calcola_scores(lista):
    scores = {}
    #Calcolo punteggi
    for persona in lista:
        score = 0
        score += pesi['pagine'] * num_pagine(persona)
        score += pesi['lingue'] * num_lingue(persona)
        score += pesi['bibliografie'] * num_bibliografie(persona)
        score += pesi['categorie'] * num_categorie(persona)
        score += pesi['sezioni'] * num_sezioni(persona)
        score += pesi['parole'] * num_parole(persona)
        scores[persona] = score
    #Creazione della classifica ordinando gli elementi in ordine decrescente
    classifica = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return classifica

scores = {}
#Calcolo punteggi
for persona in persone:
    score = 0
    score += pesi['pagine'] * num_pagine(persona)
    score += pesi['lingue'] * num_lingue(persona)
    score += pesi['bibliografie'] * num_bibliografie(persona)
    score += pesi['categorie'] * num_categorie(persona)
    score += pesi['sezioni'] * num_sezioni(persona)
    score += pesi['parole'] * num_parole(persona)
    scores[persona] = score
#Creazione della classifica ordinando gli elementi in ordine decrescente
classifica = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for pos, (persona, score) in enumerate(classifica, 1):
    print(f"{pos}. {persona}: {score:.2f}")

'''
def genrate_button():
    lista = []
    lista.append(input_one.get())
    lista.append(input_two.get())
    lista.append(input_three.get())
    lista.append(input_four.get())
    lista.append(input_five.get())
    lista.append(input_six.get())
    lista.append(input_seven.get())
    lista.append(input_eight.get())
    lista.append(input_nine.get())
    lista.append(input_ten.get())
    classifica = calcola_scores(lista)
    text_one.delete(1.0, tkinter.END)
    text_one.insert(tkinter.INSERT, classifica , "center")

root = tkinter.Tk()
root.title("Scoring&Ranking system for Wikipedia pages, by Luca Canali")

input_one = tkinter.Entry()
input_one.grid(row=0, column=1)
input_two = tkinter.Entry()
input_two.grid(row=1, column=1)


button = tkinter.Button(root, text="Generate", command=genrate_button)
button.grid(row=10, column=1)

text_one = tkinter.Text()
text_one.grid(column=1)

root.mainloop()
'''