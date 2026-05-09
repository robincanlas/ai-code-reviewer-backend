# Prerequisites

- Python v3.11+
- Ollama v0.23.2+

# Download Ollama

Mac/Linux
Install: curl -fsSL https://ollama.com/install.sh | sh

Windows:
Install: Download and install ollama from web https://ollama.com/download

Run model: ollama run deepseek-coder

# Initialize and activate venv

Mac/Linux
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

# Install Dependecies
- pip install -r requirements.txt

# Run the server
- uvicorn app.main:app --reload