import streamlit as st
from utils.story_generator import generate_story
from utils.image_generator import generate_images
from utils.comic_formatter import create_comic
from config import *

def main():
    # Add custom CSS
    st.markdown("""
        <style>
        .stTitle {
            color: #2c3e50;
            font-family: 'Comic Sans MS', cursive;
        }
        .stButton button {
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Two-column layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("ComicCrafter AI")
        st.write("Transform your ideas into comic stories! 🎨✨")
    
    with col2:
        st.image("static/logo.png", width=150)
    
    # User input
    user_prompt = st.text_area("Enter your story prompt:", height=100)
    
    if st.button("Generate Comic"):
        if not user_prompt.strip():
            st.error("Please enter a prompt first!")
            return
            
        try:
            with st.spinner("Generating your comic..."):
                # Story Generation
                st.write("📝 Creating your story...")
                story_parts = generate_story(user_prompt)
                
                # Image Generation
                st.write("🎨 Bringing your story to life...")
                images = generate_images(story_parts)
                
                # Comic Assembly
                st.write("📚 Assembling your comic...")
                comic = create_comic(story_parts, images)
                
                st.subheader("Generated Story")
                for part, text in story_parts.items():
                    st.write(f"**{part}:**")
                    st.write(text)
                
                st.subheader("Your Comic")
                st.image(comic)
                
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
            st.write("Please try again with a different prompt.")

def show_settings():
    with st.sidebar:
        st.header("Settings ⚙️")
        temperature = st.slider("Creativity Level", 0.0, 1.0, 0.7)
        style = st.selectbox(
            "Comic Style",
            ["Manga", "Western Comic", "Cartoon", "Realistic"]
        )
        return {"temperature": temperature, "style": style}

if __name__ == "__main__":
    main() 