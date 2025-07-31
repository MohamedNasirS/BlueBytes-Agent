import tensorflow as tf
from tensorflow.keras import layers, models
import pathlib

# --- Configuration ---
DATASET_DIR = pathlib.Path('dataset')
IMG_HEIGHT = 128
IMG_WIDTH = 128
BATCH_SIZE = 32
EPOCHS = 15 # Number of times to train on the entire dataset

# --- 1. Load and Prepare the Dataset ---
print("Loading dataset...")
# Create a training dataset (80% of images)
train_ds = tf.keras.utils.image_dataset_from_directory(
  DATASET_DIR,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)

# Create a validation dataset (20% of images) to test the model during training
val_ds = tf.keras.utils.image_dataset_from_directory(
  DATASET_DIR,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(IMG_HEIGHT, IMG_WIDTH),
  batch_size=BATCH_SIZE)

class_names = train_ds.class_names
print("Found classes:", class_names)

# Configure dataset for performance
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# --- 2. Define the AI Model Architecture ---
# This is a simple Convolutional Neural Network (CNN) for image analysis
model = models.Sequential([
  layers.Rescaling(1./255, input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(len(class_names) -1, activation='sigmoid') # Binary classification (genuine/tampered)
])

# --- 3. Compile the Model ---
model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
              metrics=['accuracy'])

model.summary()

# --- 4. Train the Model ---
print("\nStarting model training...")
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=EPOCHS
)

# --- 5. Save the Trained Model ---
print("\nTraining complete. Saving model...")
model.save('document_verifier.keras')
print("Model saved as 'document_verifier.keras'. It's ready to be used by the agent.")