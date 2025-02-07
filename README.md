# ComicCrafter AI

Transform your ideas into comic stories using AI! 🎨✨

## Overview
ComicCrafter AI is a generative AI-based comic generator that runs locally on edge devices. It creates comic-style stories from user prompts using:
- Mistral LLM for story generation
- Stable Diffusion for image creation
- Streamlit for the web interface

## Prerequisites
- Python 3.10
- NVIDIA GPU (tested with RTX 3060)
- 8GB+ RAM
- Git

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ComicCrafterAI.git
cd ComicCrafterAI
```

2. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required models:
   - Mistral 7B
   - Stable Diffusion 1.5 

## Usage
1. Start Stable Diffusion WebUI:
```bash
cd stable-diffusion-webui
./webui.bat --api
```

2. In another terminal, run ComicCrafterAI:
```bash
streamlit run app/main.py
```

## Project Structure
- `app/`: Main application code
  - `utils/`: Utility modules
  - `config.py`: Configuration settings
  - `main.py`: Streamlit interface
- `models/`: Model storage (not included in repo)
- `docs/`: Documentation

## License
MIT License - see LICENSE file

## Contributing
Contributions welcome! Please read CONTRIBUTING.md first. 
