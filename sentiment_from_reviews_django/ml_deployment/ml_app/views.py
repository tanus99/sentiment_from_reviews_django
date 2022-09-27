import pickle

from django.shortcuts import render
from tensorflow import keras


# Create your views here.
from tensorflow.keras.preprocessing.sequence import pad_sequences


def homepage(request):
    return render(request, 'ml_app/homepage.html')

def read_obj(path):
    with open(f'{path}.pkl', 'rb') as file:
        model = pickle.load(file)
        return model

#funzione che gestirà la predizione utilizzando il modello CNN pre-addestrato
def predict_sentiment(request):
    model = keras.models.load_model('./models/CNN')
    tokenizer = read_obj('./models/TOKENIZER')
    input = list([request.POST['frase_input']])

    frase = tokenizer.texts_to_sequences(input)
    frase = pad_sequences(frase, maxlen=508)
    # a 0.65 perchè il modello comunque non è precisissimo e si è notato
    # con delle prove che la soglia giusta per l'application è all'incirca questa
    y_preds = (model.predict(frase) > 0.5).astype('int32')
    if y_preds == 1:
        risposta = 'The sentiment is positive'
    if y_preds == 0:
        risposta = 'The sentiment is negative'
    context = {'risposta_text':risposta,'risposta_num':y_preds}
    return render(request, 'ml_app/homepage.html', context)