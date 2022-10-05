# Sentiment from reviews (Django web app)

Web app realizzata con il framework Django che integra la rete convoluzionale addestrata nella [repo](https://github.com/tanus99/sentiments_from_reviews).
L'applicazione si compone di una sola pagina web con un'area di testo all'interno della quale va inserita la recensione ***(in inglese)*** e del pulsante *Predict*
che permette di visualizzare il risultato dell'analisi.
## Authors

- [@tanus99](https://github.com/tanus99)


## Run Locally

Clona il progetto

```bash
  git clone https://github.com/tanus99/sentiments_from_reviews_django
```

Spostati nella cartella del progetto e assicurati di attivare
l'ambiente virtuale.
```bash
cd sentiments_from_reviews_django
source /bin/activate
```
Per il CNN è necessario installare le librerie *tensorflow*
e *keras*

```bash
pip install tensorflow
pip install keras
```
Installa Django con il comando
```bash
pip install django
```

Per testare la web bisogna eseguire il web server django
```bash
cd ml_deployment
python manage.py runserver
```
Accedere dal web browser inserendo nel campo url *localhost:8000/homepage*

## Screenshots
![good](/sentiment_from_reviews_django/good_review.png)
![bad](/sentiment_from_reviews_django/bad_review.png)

## License
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
