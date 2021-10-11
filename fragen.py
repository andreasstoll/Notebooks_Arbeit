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
    
    check = widgets.Button(description="submit")
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
    print("Wird die Frage durch kategoriale oder quantitative Daten beantwortet?")
    display(Q3)
    display(Q4)
    display(Q5)


