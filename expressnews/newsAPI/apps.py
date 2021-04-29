import os
import keras
import tensorflow as tf
from django.apps import AppConfig
from django.conf import settings


class NewsapiConfig(AppConfig):
    name = 'newsAPI'
    path = os.path.join(settings.MODELS, "news_text_classification.h5") 
   
    loaded_model=tf.keras.models.load_model(path)