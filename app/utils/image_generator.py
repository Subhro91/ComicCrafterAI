import requests
from typing import Dict, List
from PIL import Image
import io
import base64
import config

class ImageGenerator:
    def __init__(self):
        self.api_url = config.STABLE_DIFFUSION_URL
        self.image_size = config.IMAGE_SIZE

    def _create_prompt(self, text: str, part: str) -> str:
        """Create specific prompts for each story part"""
        # Base style that works well with Stable Diffusion
        style_prompt = "masterpiece, best quality, highly detailed, digital art, comic book style"
        
        # Extract key subjects from text (first 100 characters should contain main subjects)
        key_subjects = text[:100].replace(".", "").strip()
        
        if part == 'Introduction':
            return f"{key_subjects}, {style_prompt}, establishing shot, full scene, clear view of characters and setting, soft lighting, <lora:more_details:0.6>"
        elif part == 'Storyline':
            return f"{key_subjects}, {style_prompt}, action shot, character interaction, dynamic pose, detailed environment, <lora:more_details:0.6>"
        elif part == 'Climax':
            return f"{key_subjects}, {style_prompt}, dramatic moment, intense action, dramatic lighting, emotional expression, <lora:more_details:0.6>"
        else:  # Moral
            return f"{key_subjects}, {style_prompt}, meaningful scene, emotional moment, character focus, warm lighting, <lora:more_details:0.6>"

    def _generate_single_image(self, prompt: str) -> Image.Image:
        """Generate a single image using Stable Diffusion"""
        try:
            payload = {
                "prompt": prompt,
                "negative_prompt": "text, watermark, low quality, blurry, distorted, disfigured, bad anatomy, ugly, duplicate, error, out of frame, extra limbs, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, mutated hands, fused fingers, too many fingers, long neck",
                "steps": 35,
                "width": 768,
                "height": 768,
                "sampler_name": "DPM++ 2M Karras",
                "cfg_scale": 9,            # Increased for better prompt adherence
                "restore_faces": True,
                "denoising_strength": 0.6,  # Reduced for more stable output
                "clip_skip": 2,            # Better for artistic styles
            }

            response = requests.post(
                url=f"{self.api_url}/sdapi/v1/txt2img",
                json=payload
            )

            if response.status_code == 200:
                r = response.json()
                image_bytes = base64.b64decode(r['images'][0])
                image = Image.open(io.BytesIO(image_bytes))
                return image
            else:
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            print(f"Error generating image: {str(e)}")
            return None

    def generate_images(self, story_parts: Dict[str, str]) -> List[Image.Image]:
        """Generate images for each story part"""
        images = []
        for part, text in story_parts.items():
            prompt = self._create_prompt(text, part)
            image = self._generate_single_image(prompt)
            if image:
                images.append(image)
            else:
                img = Image.new('RGB', self.image_size, 'white')
                images.append(img)
        return images

# Function to be imported by main.py
def generate_images(story_parts: Dict[str, str]) -> List[Image.Image]:
    generator = ImageGenerator()
    return generator.generate_images(story_parts) 