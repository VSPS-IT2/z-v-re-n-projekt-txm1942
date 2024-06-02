from flask import Flask, render_template

projekt = Flask(__name__)

@projekt.route('/')
def ProjektZ():
    
    vysledky1 = [
        {'sport': 'Fotbal', 'Výsledky': 'Borussia Dortmund vs. Real Madrid: 0-2'},
        {'sport': 'Hokej', 'Výsledky': 'Boston Bruins vs. New York Rangers: 2-5'},
        {'sport': 'Tenis', 'Výsledky': 'Arnaldi M. vs. Tsitsipas S.: 	1-3'}
    ] 

    return render_template('index.html', vysledky1=vysledky1)

if __name__ == '__main__':
    projekt.run(debug=True)
