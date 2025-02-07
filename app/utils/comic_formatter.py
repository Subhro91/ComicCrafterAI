from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List
import config

class ComicFormatter:
    def __init__(self):
        self.width = config.COMIC_WIDTH
        self.height = config.COMIC_HEIGHT
        self.panels_per_page = config.PANELS_PER_PAGE

    def _create_panel(self, image: Image.Image, text: str) -> Image.Image:
        """Create a single comic panel with image and text"""
        panel = Image.new('RGB', (self.width // 2, self.height // 2), 'white')
        # Add image
        if image:
            # Resize and paste image
            image = image.resize((panel.width, int(panel.height * 0.7)))
            panel.paste(image, (0, 0))

        # Add text
        draw = ImageDraw.Draw(panel)
        # TODO: Add proper font handling
        # font = ImageFont.truetype("path/to/comic/font.ttf", 20)
        draw.text((10, panel.height - 50), text[:100] + "...", fill="black")
        
        return panel

    def create_comic(self, story_parts: Dict[str, str], images: List[Image.Image]) -> Image.Image:
        """Create a comic page from story parts and images"""
        comic = Image.new('RGB', (self.width, self.height), 'white')
        
        # Create panels
        panels = []
        for (part, text), image in zip(story_parts.items(), images):
            panel = self._create_panel(image, text)
            panels.append(panel)

        # Arrange panels in 2x2 grid
        for i, panel in enumerate(panels):
            x = (i % 2) * (self.width // 2)
            y = (i // 2) * (self.height // 2)
            comic.paste(panel, (x, y))

        return comic

# Function to be imported by main.py
def create_comic(story_parts: Dict[str, str], images: List[Image.Image]) -> Image.Image:
    formatter = ComicFormatter()
    return formatter.create_comic(story_parts, images) 