import os
from llama_cpp import Llama
from typing import Dict
import config

class StoryGenerator:
    def __init__(self):
        # Initialize the LLM model
        if not os.path.exists(config.LLM_MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {config.LLM_MODEL_PATH}")
        
        self.llm = Llama(
            model_path=config.LLM_MODEL_PATH,
            n_ctx=512,          
            n_threads=8,        
            n_batch=512,        
            n_gpu_layers=-1,    # Use all layers on GPU (-1 means use all)
            use_mlock=True,     
            use_mmap=True,
            offload_kqv=True    # Offload key/query/value to GPU
        )

    def generate(self, prompt: str) -> Dict[str, str]:
        """Generate a story from the given prompt"""
        formatted_prompt = f"""Create a visual story about: {prompt}

Write a complete story with these EXACT sections. Each section must have 2-3 descriptive sentences:

INTRODUCTION:
[Write the opening scene, describing what we see]

STORYLINE:
[Write the main action, describing what happens]

CLIMAX:
[Write the peak moment, describing the most dramatic scene]

MORAL:
[Write the ending scene that shows the lesson]

Focus on visual details we can see. Be specific and descriptive."""
        
        response = self.llm.create_completion(
            formatted_prompt,
            max_tokens=750,      # Increased for fuller stories
            temperature=0.8,     # Slightly more creative
            stop=["You are", "[Write"],
            echo=False
        )
        
        # Parse the response
        story_text = response['choices'][0]['text']
        story_parts = self.parse_story(story_text)
        
        # Ensure all parts exist
        required_parts = ['Introduction', 'Storyline', 'Climax', 'Moral']
        for part in required_parts:
            if part not in story_parts:
                story_parts[part] = f"Default {part.lower()} text."
        
        return story_parts

    def parse_story(self, text: str) -> Dict[str, str]:
        """Parse the LLM output into story parts"""
        parts = {}
        current_part = None
        current_text = []
        
        # Debug print
        print("Raw text received:", text)
        
        # Clean up the text
        text = text.strip()
        if not text:
            return {'Introduction': 'Default introduction', 'Storyline': 'Default storyline', 
                   'Climax': 'Default climax', 'Moral': 'Default moral'}

        # Split and process lines
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check for section headers
            if "INTRODUCTION:" in line.upper():
                if current_part and current_text:
                    parts[current_part] = ' '.join(current_text).strip()
                current_part = 'Introduction'
                current_text = []
            elif "STORYLINE:" in line.upper():
                if current_part and current_text:
                    parts[current_part] = ' '.join(current_text).strip()
                current_part = 'Storyline'
                current_text = []
            elif "CLIMAX:" in line.upper():
                if current_part and current_text:
                    parts[current_part] = ' '.join(current_text).strip()
                current_part = 'Climax'
                current_text = []
            elif "MORAL:" in line.upper():
                if current_part and current_text:
                    parts[current_part] = ' '.join(current_text).strip()
                current_part = 'Moral'
                current_text = []
            # Only add lines that aren't section headers and aren't placeholders
            elif current_part and not any(marker in line for marker in ['[', ']', 'Default']):
                current_text.append(line)
        
        # Don't forget to add the last section
        if current_part and current_text:
            parts[current_part] = ' '.join(current_text).strip()
        
        # Debug print
        print("Parsed parts:", parts)
        
        # Only use defaults for truly missing or empty parts
        required_parts = ['Introduction', 'Storyline', 'Climax', 'Moral']
        for part in required_parts:
            if part not in parts or not parts[part] or parts[part].isspace():
                print(f"Missing {part}, using default")
                parts[part] = f"A {part.lower()} scene showing the story's {part.lower()}."
        
        return parts

# Create a function to be imported by main.py
def generate_story(prompt: str) -> Dict[str, str]:
    generator = StoryGenerator()
    return generator.generate(prompt) 