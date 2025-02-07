# Configuration settings for ComicCrafter AI

# LLM Settings
LLM_MODEL_PATH = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
MAX_TOKENS = 512
TEMPERATURE = 0.7

# Image Generation Settings
STABLE_DIFFUSION_URL = "http://127.0.0.1:7860"
IMAGE_SIZE = (768, 768)

# Comic Settings
PANELS_PER_PAGE = 4
COMIC_WIDTH = 1536
COMIC_HEIGHT = 1536

# System Messages
STORY_PROMPT_TEMPLATE = """
Create a 4-part story based on the following prompt. 
The parts should be:
1. Introduction
2. Storyline development
3. Climax
4. Moral of the story

User prompt: {user_prompt}

Format the response as:
INTRODUCTION:
[introduction text]
STORYLINE:
[storyline text]
CLIMAX:
[climax text]
MORAL:
[moral text]
"""

# Quality Settings
IMAGE_QUALITY = {
    "steps": 35,
    "cfg_scale": 9,
    "denoising_strength": 0.6,
    "clip_skip": 2
} 