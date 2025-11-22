import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
import os

# --- CONFIGURATION ---
DATASET_PATH = 'isl_dataset' 
IMG_HEIGHT = 64
IMG_WIDTH = 64
IMAGES_PER_BATCH = 32

print("Checking for dataset...")
if not os.path.exists(DATASET_PATH):
    print(f"ERROR: The folder '{DATASET_PATH}' was not found.")
    print("Please make sure your dataset folder is inside the project folder.")
    exit()

# --- 1. LOAD DATA ---
print("Loading images from disk...")
# Training Data (80%)
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    images_per_batch=IMAGES_PER_BATCH,
    color_mode='grayscale'
)

# Validation Data (20%)
val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    images_per_batch=IMAGES_PER_BATCH,
    color_mode='grayscale'
)

class_names = train_ds.class_names
print(f"Found {len(class_names)} classes: {class_names}")

# Optimization (makes loading faster)
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# --- 2. BUILD THE MODEL (THE BRAIN) ---
print("Building the model...")
model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(IMG_HEIGHT, IMG_WIDTH, 1)),
    
    # Layer 1: Seeing basic shapes
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    
    # Layer 2: Seeing complex shapes
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    
    # Layer 3: Seeing abstract concepts
    layers.Conv2D(128, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5), # Prevents overfitting
    layers.Dense(len(class_names), activation='softmax') # Output layer
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])

model.summary()

# --- 3. TRAIN THE MODEL ---
print("Starting training... (This may take a while)")
epochs = 18
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)

# --- 4. SAVE THE MODEL ---
print("Saving the model...")
model.save('isl_model.h5')
print("SUCCESS! Model saved as 'isl_model.h5'")

# --- 5. CREATE REPORT GRAPH ---
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.savefig('training_graph.png')
print("Graph saved as 'training_graph.png'")