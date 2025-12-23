# Poem to Video (poem-mp4) 🎬📜

A Python-based utility that generates a premium, bilingual (French & Portuguese) video from a romantic poem using **MoviePy 2.0+**.

## Features

- **Bilingual Display**: Shows both original French and Portuguese translation simultaneously.
- **Premium Aesthetics**: Artistic background with a Ken Burns (slow zoom) effect.
- **Cinematic Transitions**: Smooth crossfades (1.2s) between stanzas.
- **Audio Integration**: Automatically syncs with background music (`someday.mp3`).
- **Unicode Support**: Full support for French and Portuguese accent marks using elegant serif typography.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd poem-mp4
   ```

2. **Virtual Environment**:
   Ensure you have a virtual environment with the required dependencies:
   ```bash
   python -m venv .env
   .\.env\Scripts\activate
   pip install moviepy
   ```

3. **Run the script**:
   Place your audio file as `someday.mp3` and run:
   ```bash
   python poema.py
   ```

## Requirements

- Python 3.10+
- MoviePy 2.0.0+
- FFmpeg (installed and in PATH)
