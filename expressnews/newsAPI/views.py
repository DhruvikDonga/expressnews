from django.shortcuts import render
import json
from django.shortcuts import get_object_or_404
# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Newsapi
from .serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from rest_framework import status
import pickle
import numpy as np 
from tensorflow.keras.preprocessing.sequence import pad_sequences
from .apps import NewsapiConfig
import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import word_tokenize
from django.conf import settings
import os
class ListNewsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Newsapi.objects.all().order_by('-created')
    serializer_class = NewsSerializer

@api_view(['POST'])
def getfavourite(request):
    
    body = json.loads(request.body)
    if "userid" in body and "newsid" in body:
        user = User.objects.get(id = body["userid"])
        savenews = get_object_or_404(Newsapi, pk=body['newsid'])
        if savenews.favourite.filter(id=body["userid"]).exists():
            savenews.favourite.remove(user)
            return Response("Deleted", status=status.HTTP_201_CREATED)

        else:
            savenews.favourite.add(user)
            serializer = NewsSerializer(savenews)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getfavouritenews(request):
    permission_classes = (IsAuthenticated,)
    userid = request.user.id
    queryset = User.objects.get(id = userid).news_favourite.all().order_by('-created')
    serializer = NewsSerializer(queryset, many=True)
    return Response(serializer.data)   
    



stop_words = set(stopwords.words('english'))
def clean(text):
    # Lowering letters
    text = text.lower()
    # Removing html tags
    text = re.sub('<[^>]*>', '', text)
    # Removing emails
    text = re.sub('\S*@\S*\s?', '', text)
    # Removing urls
    text = re.sub('https?://[A-Za-z0-9]','',text)
    # Removing numbers
    text = re.sub('[^a-zA-Z]',' ',text)
    word_tokens = word_tokenize(text)    
    filtered_sentence = []
    for word_token in word_tokens:
        if word_token not in stop_words:
            filtered_sentence.append(word_token)
    
    # Joining words
    text = (' '.join(filtered_sentence))
    return text



def predict(scrapped_articles):

    all_cleaned_texts = np.array([clean(text) for text in scrapped_articles])
    path = os.path.join(settings.MODELS, "tokenizer.pickle") 
    with open(path, 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    all_cleaned_sequences = tokenizer.texts_to_sequences(all_cleaned_texts)
    all_cleaned_padded = pad_sequences(all_cleaned_sequences, maxlen=300, padding="pre", truncating="post")
    
    predictions = NewsapiConfig.loaded_model.predict(all_cleaned_padded)
    path = os.path.join(settings.MODELS, "encoder")
    with open(path, 'rb') as handle:
        one_hot_encoder = pickle.load(handle)
    predictions = one_hot_encoder.inverse_transform(predictions)
    return predictions[0][0]