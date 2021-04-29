from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import model_from_json
def loadmodel():
    path = os.path.join( "news_text_classification.h5") 
    new_model = load_model(path)
    print(new_model.summary())