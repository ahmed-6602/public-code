import tensorflow as tf
from tensorflow.keras import layers
# Create a simple neural network
model = tf.keras.Sequential([
 layers.Dense(64, activation='relu',
input_shape=(784,)),
 layers.Dense(10, activation='softmax')
])
# Compile the model
model.compile(optimizer='adam',
 loss='sparse_categorical_crossentropy',
 metrics=['accuracy'])
#Train the model (example data used here)
model.fit(train_data, train_labels, epochs=10,batch_size=32)
