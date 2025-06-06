import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


model = tf.keras.models.load_model('pokemon_type_classifier.h5')
class_names = ['eau', 'eclair', 'feu', 'flying', 'terre']


def predict_pokemon_type(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    confidence = predictions[0][class_index]
    return class_names[class_index], confidence


def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
 
        img = Image.open(file_path)
        img = img.resize((150, 150))
        img_tk = ImageTk.PhotoImage(img)
        panel.configure(image=img_tk)
        panel.image = img_tk


        prediction, confidence = predict_pokemon_type(file_path)
        result_label.config(text=f"Type : {prediction}\nConfiance : {confidence*100:.2f}%")


root = tk.Tk()
root.title(" Projet IA : Classification de Pokémon par Type")

window_width = 400
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
btn = tk.Button(root, text="Choisir une image", command=select_image)
btn.pack(pady=10)


panel = tk.Label(root)
panel.pack()


result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)


root.mainloop()
