import wikipediaapi
import tkinter

wiki = wikipediaapi.Wikipedia('it')
#Lista di persone di interesse
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

'''scores = {}
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
    print(f"{pos}. {persona}: {score:.2f}")'''

root = tkinter.Tk()
root.title("Scoring&Ranking system for Wikipedia pages, by Luca Canali")

input_one = tkinter.Entry()
input_one.grid(row=0, column=1)
input_two = tkinter.Entry()
input_two.grid(row=1, column=1)
input_three = tkinter.Entry()
input_three.grid(row=2, column=1)
input_four = tkinter.Entry()
input_four.grid(row=3, column=1)
input_five = tkinter.Entry()
input_five.grid(row=4, column=1)
input_six = tkinter.Entry()
input_six.grid(row=5, column=1)
input_seven = tkinter.Entry()
input_seven.grid(row=6, column=1)
input_eight = tkinter.Entry()
input_eight.grid(row=7, column=1)
input_nine = tkinter.Entry()
input_nine.grid(row=8, column=1)
input_ten = tkinter.Entry()
input_ten.grid(row=9, column=1)

button = tkinter.Button(root, text="Generate" ''' command=start()''')
button.grid(row=10, column=1)

text_one = tkinter.Text()
text_one.grid(column=1)
root.mainloop()