import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

# Create a simple neural network
model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(784,)),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Example training data
train_data = np.random.rand(1000, 784)       # 1000 samples, each with 784 features
train_labels = np.random.randint(10, size=1000)  # 1000 labels (0-9)

# Train the model
model.fit(train_data, train_labels, epochs=10, batch_size=32)
