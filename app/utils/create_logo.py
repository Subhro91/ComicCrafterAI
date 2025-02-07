from PIL import Image, ImageDraw, ImageFont
import os

def create_logo():
    # Create a new image with a white background
    img = Image.new('RGB', (300, 150), 'white')
    draw = ImageDraw.Draw(img)
    
    # Add text
    text = "Comic\nCrafter"
    draw.text((20, 20), text, fill='black', spacing=10, align="center")
    
    # Ensure static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Save the image
    img.save('static/logo.png')

if __name__ == "__main__":
    create_logo() 