from typing import Dict, List
from PIL import Image

def generate_test_story() -> Dict[str, str]:
    """Generate a test story for development"""
    return {
        'Introduction': 'A curious cat named Whiskers lived by the ocean.',
        'Storyline': 'Every day, Whiskers watched the fish swim, wishing to join them.',
        'Climax': 'One stormy day, Whiskers finally gathered the courage to jump in.',
        'Moral': 'Bravery helps us overcome our fears and achieve our dreams.'
    }

def generate_test_images() -> List[Image.Image]:
    """Generate test images for development"""
    # Create simple colored rectangles as placeholder images
    images = []
    colors = ['red', 'blue', 'green', 'yellow']
    
    for color in colors:
        img = Image.new('RGB', (512, 512), color)
        images.append(img)
    
    return images 