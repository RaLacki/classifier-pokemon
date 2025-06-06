import tensorflow as tf 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os


data_dir ="data"
img_height,img_width =150,150
batch_size=32
epochs=30


datagen =ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    validation_split=0.2,
    horizontal_flip=True,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.1,
    brightness_range=(0.8, 1.2)
)
train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training',
    shuffle=True
)
validation_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3), activation='relu', input_shape=(img_height, img_width, 3)),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(5, activation='softmax') 
])
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()


model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)


model.save("pokemon_type_classifier.h5")
print("✅ Modèle sauvegardé sous 'pokemon_type_classifier.h5'")