# Tie and Jon Pygame Project

A simple Pygame project.

## Setup Instructions

### 1. Prerequisites
- Python 3.x installed.

### 2. Create and Activate Virtual Environment (Optional but Recommended)

**Windows:**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Note: This project uses `pygame-ce` (Community Edition), which is a drop-in replacement for `pygame` with more frequent updates and better performance.

### 4. Run the Game
```bash
python main.py
```

## Troubleshooting
If you encounter issues with `pygame-ce` installation on Linux, you may need to install additional system dependencies (e.g., `libsdl2-dev`, `libsdl2-image-dev`, `libsdl2-mixer-dev`, `libsdl2-ttf-dev`).
