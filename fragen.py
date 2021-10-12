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
    Q4 = create_multipleChoice_widget('Welcher der folgenden Codes ruft das Alter von Billie ab?',['animal_table.loc["Billie"]Alter', 'animal_table.loc[Billie]Alter', 'animal_table.loc[Billie].Alter' 'animal_table.loc["Billie"].Alter'],'animal_table.loc["Billie"].Alter')


    display(Q1)
    display(Q2)
    display(Q3)
    display(Q4)