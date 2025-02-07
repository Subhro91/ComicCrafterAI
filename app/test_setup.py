import os
import sys
from utils.story_generator import generate_story
from utils.image_generator import generate_images
from utils.comic_formatter import create_comic
from config import *

def test_imports():
    print("Testing imports and configurations...")
    print(f"LLM Model Path: {LLM_MODEL_PATH}")
    print(f"Model exists: {os.path.exists(LLM_MODEL_PATH)}")
    print("\nAll imports successful!")

def test_story_generation():
    print("\nTesting story generation...")
    try:
        test_prompt = "A story about a brave cat who learns to swim"
        story = generate_story(test_prompt)
        print("Story generation successful!")
        print("\nGenerated story parts:")
        for part, text in story.items():
            print(f"\n{part}:")
            print(text)
    except Exception as e:
        print(f"Error in story generation: {str(e)}")

def check_model():
    print(f"Checking for model at: {LLM_MODEL_PATH}")
    if os.path.exists(LLM_MODEL_PATH):
        print("✅ Model found!")
        print(f"Model size: {os.path.getsize(LLM_MODEL_PATH) / (1024*1024*1024):.2f} GB")
        return True
    else:
        print("❌ Model not found!")
        print(f"Please ensure the model is downloaded to: {LLM_MODEL_PATH}")
        return False

if __name__ == "__main__":
    check_model()
    test_imports()
    test_story_generation() 