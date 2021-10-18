#Source: https://github.com/jupyter-widgets/ipywidgets/issues/2487

import ipywidgets as widgets
from IPython.display import display
from IPython.display import clear_output

def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Richtig." + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Falsch. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="Überprüfen")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])

def fragen1():
    Q1 = create_multipleChoice_widget('Was für ein Datentyp ist der "Name" eines Autos?',['kategorial', 'quantitativ'],'kategorial')
    Q2 = create_multipleChoice_widget('Was für ein Datentyp ist der "Preis" eines Autos?',['kategorial', 'quantitativ'],'quantitativ')
    Q3 = create_multipleChoice_widget('Was ist die häufigste Autofarbe?',['kategorial', 'quantitativ'],'kategorial')
    Q4 = create_multipleChoice_widget('Welches Auto ist am ältesten?',['kategorial', 'quantitativ'],'quantitativ')
    Q5 = create_multipleChoice_widget('Wieviele Autos haben eine manuelle Schaltung?',['kategorial', 'quantitativ'],'kategorial')


    display(Q1)
    display(Q2)
    print("Werden die folgenden drei Fragen durch kategoriale oder quantitative Daten beantwortet?\n")
    display(Q3)
    display(Q4)
    display(Q5)

def fragen2():
    Q1 = create_multipleChoice_widget('Für welchen Datentyp eignet sich ein Kuchendiagramm?',['kategorial', 'quantitativ'],'kategorial')
    Q2 = create_multipleChoice_widget('Für welchen Datentyp eignet sich ein Histogramm?',['kategorial', 'quantitativ'],'quantitativ')
    Q3 = create_multipleChoice_widget('Was ist die Bedeutung der 4 bei histogram(animal_table, "Beine", 4)?',['maximale Anzahl Beine', 'minimale Anzahl Beine', 'Anzahl Rechtecke'],'Anzahl Rechtecke')

    display(Q1)
    display(Q2)
    display(Q3)



def fragen3():
    Q1 = create_multipleChoice_widget('Welcher der folgenden Codes ruft die Zeile von Snowcone richtig ab?',['animal_table.loc[Snowcone]', 'animal_table["Snowcone"]', 'animal_table.loc["Snowcone"]', 'animal_table[Snowcone]'],'animal_table.loc["Snowcone"]')
    Q2 = create_multipleChoice_widget('Welches Attribut ruft der folgende Code ab: ''animal_table.loc["Snowcone"].Geschlecht'' ?',['Das Geschlecht von Bo', 'Das Alter von Bo', 'Das Geschlecht von Snowcone', 'Das Alter von Snowcone'],'Das Geschlecht von Snowcone')
    Q3 = create_multipleChoice_widget('Was muss vorher geschehen sein, damit Bo.Alter das Alter von Bo abruft?',['Die Variable Bo muss definiert werden', 'Die Variable Alter muss definiert werden'],'Die Variable Bo muss definiert werden')
    Q4 = create_multipleChoice_widget('Welcher der folgenden Codes ruft das Alter von Billie ab?',['animal_table.loc["Billie"]Alter', 'animal_table.loc[Billie]Alter', 'animal_table.loc[Billie].Alter', 'animal_table.loc["Billie"].Alter'],'animal_table.loc["Billie"].Alter')


    display(Q1)
    display(Q2)
    display(Q3)
    display(Q4)

def fragen1a():
    Q1 = create_multipleChoice_widget('Haarfarbe',['kategorial', 'quantitativ'],'kategorial')
    Q2 = create_multipleChoice_widget('Postleitzahl',['kategorial', 'quantitativ'],'kategorial')
    Q3 = create_multipleChoice_widget('Geburtsort',['kategorial', 'quantitativ'],'kategorial')
    Q4 = create_multipleChoice_widget('Grösse',['kategorial', 'quantitativ'],'quantitativ')
    Q5 = create_multipleChoice_widget('Gewicht',['kategorial', 'quantitativ'],'quantitativ')
    Q6 = create_multipleChoice_widget('Wohnort',['kategorial', 'quantitativ'],'kategorial')

    display(Q1)
    display(Q2)
    display(Q3)
    display(Q4)
    display(Q5)
    display(Q6)


def fragen10(a1, a2, a3):
    Q1 = create_multipleChoice_widget('Form?',['linear', 'nicht-linear', 'keine'], a1)
    Q2 = create_multipleChoice_widget('Richtung?',['steigend', 'fallend', 'keine'], a2)
    Q3 = create_multipleChoice_widget('Stärke?',['stark', 'schwach'], a3)

    display(Q1)
    display(Q2)
    display(Q3)

def frage10A():
    fragen10("linear", "fallend", "stark")

def frage10B():
    fragen10("keine", "keine", "schwach")

def frage10C():
    fragen10("linear", "steigend", "stark")

def frage10D():
    fragen10("keine", "steigend", "schwach")

def frage10E():
    fragen10("nicht-linear", "keine", "stark")

def frage10F():
    fragen10("linear", "fallend", "schwach")

def fragen11(a1, a2, a3):
    Q1 = create_multipleChoice_widget('Steigung?',['steigt', 'fällt'], a1)
    Q2 = create_multipleChoice_widget('Stärke?',['stark', 'schwach'], a2)
    Q3 = create_multipleChoice_widget('Korrelationskoeffizient r?',['ca. -1', 'ca .-0.5', 'ca. 0', 'ca. 0.5', 'ca. 1'], a3)

    display(Q1)
    display(Q2)
    display(Q3)

def frage11A():
    fragen11("steigt", "stark", "ca. 1")

def frage11B():
    fragen11("steigt", "schwach", "ca. 0.5")

def frage11C():
    fragen11("steigt", "stark", "ca. 1")

def frage11D():
    fragen11("fällt", "stark", "ca. -1")

def frage11lra():
    Q1 = create_multipleChoice_widget('Die Regressionsgerade ...',['steigt', 'fällt'],'fällt')
    Q2 = create_multipleChoice_widget('Die Korrelation ist ...',['stark', 'schwach', 'fast nicht existent'],'fast nicht existent')
    
    display(Q1)
    display(Q2)

def frage11lrb():
    Q1 = create_multipleChoice_widget('Person A hat eine grössere Schuhgrösse als Person B. Es wird erwartet, dass A ...',['grösser ist', 'kleiner ist'],'grösser ist')
    Q2 = create_multipleChoice_widget('Die Korrelation ist ...',['stark', 'schwach', 'fast nicht existent'],'stark')
    
    display(Q1)
    display(Q2)

def frage11lrc():
    Q1 = create_multipleChoice_widget('Die Beziehung ist ...',['stark', 'schwach', 'fast nicht existent'],'fast nicht existent')
    
    display(Q1)

def frage11lrd():
    Q1 = create_multipleChoice_widget('Die Korrelation ist ...',['stark', 'moderat', 'schwach'],'moderat')
    Q2 = create_multipleChoice_widget('Pro verpasste Schulwoche fällt der Durschnitt um ...',['0.26 Punkte', '6.34 Punkte'],'0.26 Punkte')
    
    display(Q1)
    display(Q2)