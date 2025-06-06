import tensorflow as tf 
from tensorflow.keras.preprocessing import image
import numpy as np 
import os

model = tf.keras.models.load_model('pokemon_type_classifier.h5')

class_names= ['eau','eclair','feu','flying','terre']

def predict_pokemon_type(img_path):
    img= image.load_img(img_path,target_size=(150,150))
    img_array =image.img_to_array(img)
    img_array=img_array/255.0
    img_array= np.expand_dims(img_array,axis=0)

    predictions =model.predict(img_array)
    class_index = np.argmax(predictions)
    confidence = predictions[0][class_index]

    print(f"Image : {os.path.basename(img_path)}")
    print(f"Prédiction : {class_names[class_index]} avec une confiance de {confidence*100:.2f}%")

if __name__ == "__main__":
    test_image_path = input("veuillez coller le chemin vers l'image de votre POKEMON")
    predict_pokemon_type(test_image_path)