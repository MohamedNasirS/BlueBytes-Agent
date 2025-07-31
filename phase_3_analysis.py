import tensorflow as tf
import numpy as np

MODEL_PATH = 'document_verifier.keras'
IMG_HEIGHT = 128
IMG_WIDTH = 128
CLASS_NAMES = ['genuine', 'tampered']

print("Loading verification model...")
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"WARNING: Could not load model from {MODEL_PATH}. Verification will fail.")
    model = None

def predict_authenticity(document_path):
    """Analyzes the document using the trained AI model."""
    if model is None:
        return False

    try:
        img = tf.keras.utils.load_img(
            document_path, target_size=(IMG_HEIGHT, IMG_WIDTH)
        )
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = model.predict(img_array)
        score = predictions[0][0]
        
        predicted_class = CLASS_NAMES[int(round(score))]
        
        if predicted_class == 'tampered':
            return False
        else:
            return True
    except Exception as e:
        print(f"Error during prediction: {e}")
        return False