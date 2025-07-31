from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import random
import os

TEMPLATE_PATH = 'dataset/tampered/tampered_doc_2.png'
OUTPUT_DIR = 'dataset'
GENUINE_DIR = os.path.join(OUTPUT_DIR, 'genuine')
TAMPERED_DIR = os.path.join(OUTPUT_DIR, 'tampered')
NUM_GENUINE = 150
NUM_TAMPERED = 150
FONT_PATH = "C:/Windows/Fonts/arial.ttf"
TAMPER_FONT_PATH = "C:/Windows/Fonts/cour.ttf" # For Courier New
FONT_SIZE = 18

fake = Faker('en_IN')

def generate_pan_number():
    pan = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
    pan += ''.join(random.choices('0123456789', k=4))
    pan += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return pan

def create_card(is_tampered=False):
    try:
        img = Image.open(TEMPLATE_PATH).convert("RGB")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        tamper_font = ImageFont.truetype(TAMPER_FONT_PATH, FONT_SIZE + 2)
    except FileNotFoundError:
        print(f"ERROR: Template '{TEMPLATE_PATH}' or font '{FONT_PATH}' not found.")
        return None, None

    name = fake.name().upper()
    father_name = fake.name().upper()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=70).strftime("%d/%m/%Y")
    pan_num = generate_pan_number()

    fields = {
        "name": (name, (40, 140)),
        "father_name": (father_name, (40, 180)),
        "dob": (dob, (40, 230)),
        "pan": (pan_num, (40, 280))
    }
    
    if is_tampered:
        field_to_tamper = random.choice(list(fields.keys()))
        tamper_type = random.choice(["font", "misalignment"])
        
        for key, (text, pos) in fields.items():
            current_font = font
            current_pos = pos
            if key == field_to_tamper:
                if tamper_type == "font":
                    current_font = tamper_font
                elif tamper_type == "misalignment":
                    current_pos = (pos[0], pos[1] + 5)
            draw.text(current_pos, text, font=current_font, fill="black")
    else:
        for key, (text, pos) in fields.items():
            draw.text(pos, text, font=font, fill="black")

    return img, f"{pan_num}.png"

if __name__ == "__main__":
    os.makedirs(GENUINE_DIR, exist_ok=True)
    os.makedirs(TAMPERED_DIR, exist_ok=True)

    print(f"Generating {NUM_GENUINE} genuine documents...")
    for i in range(NUM_GENUINE):
        card_img, filename = create_card(is_tampered=False)
        if card_img: card_img.save(os.path.join(GENUINE_DIR, filename))

    print(f"Generating {NUM_TAMPERED} tampered documents...")
    for i in range(NUM_TAMPERED):
        card_img, filename = create_card(is_tampered=True)
        if card_img: card_img.save(os.path.join(TAMPERED_DIR, filename))

    print("\nDataset generation complete.")