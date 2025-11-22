import cv2
import numpy as np
import tensorflow as tf
import os

# --- LOAD BRAIN ---
model = tf.keras.models.load_model('isl_model.h5')
class_names = sorted(os.listdir('isl_dataset'))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --- 1. MIRROR FIX ---
    # If you use RIGHT HAND, do NOT flip.
    # If you use LEFT HAND, uncomment the line below:
    # frame = cv2.flip(frame, 1)

    # --- 2. ROI (The Box) ---
    # Using the exact coordinates that worked best for you
    roi = frame[100:400, 100:400]
    cv2.rectangle(frame, (100, 100), (400, 400), (255, 0, 0), 3)

    # --- 3. RAW PRE-PROCESSING (Matches Training Exactly) ---
    # Convert to Grayscale
    img_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # Resize to 64x64
    img_resized = cv2.resize(img_gray, (64, 64))
    
    # Normalize (Divide by 255). This is CRITICAL.
    # The training script used 'Rescaling(1./255)', so we MUST do it here too.
    img_processed = img_resized.astype('float32') / 255.0
    img_processed = np.expand_dims(img_processed, axis=0)
    img_processed = np.expand_dims(img_processed, axis=-1)

    # --- 4. PREDICT ---
    prediction = model.predict(img_processed, verbose=0)
    index = np.argmax(prediction)
    label = class_names[index]
    confidence = prediction[0][index]

    # --- 5. DISPLAY ---
    text = f"Sign: {label} ({int(confidence*100)}%)"
    
    if confidence > 0.6:
        color = (0, 255, 0) # Green
    else:
        color = (0, 255, 255) # Yellow

    cv2.putText(frame, text, (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    
    # Show Main Window
    cv2.imshow('ISL Detector', frame)
    
    # Show the RAW Brain View (Should look soft and grey, not sharp white)
    cv2.imshow('Raw Brain View', img_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()