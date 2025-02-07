import streamlit as st

def show_progress(stage: str, progress: float, status_text: str = ""):
    """Show detailed progress with status text"""
    stages = {
        "story": "📝 Generating Story...",
        "images": "🎨 Creating Artwork...",
        "comic": "📚 Assembling Comic..."
    }
    
    st.progress(progress)
    st.write(f"Current Stage: {stages.get(stage, stage)}")
    if status_text:
        st.write(status_text) 