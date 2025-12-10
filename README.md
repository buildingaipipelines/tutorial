## AI Pipeline Tutorial Code

This folder contains the **Python implementation** that accompanies the “Build Real AI Systems” tutorial.  
Readers download this code bundle while working through the tutorial and run it locally step by step.

## Contents

- `src/` – Python modules described in the tutorial:
  - `ingest.py`, `transform.py`, `generate.py`, `evaluate.py`, `save.py`, `process.py`, `config.py`, `test_openai.py`, `__init__.py`
- `data/` – sample input CSV (`input.csv`)
- `output/` – output folder (created/used by the pipeline)
- `logs/` – log folder (used by logging helpers)
- `run_pipeline.py` – single entry point for running the whole pipeline
- `requirements.txt` – Python dependencies
- `.env.example` – example environment-variable file
- `README.md` – this file

## How to run the Python pipeline

From inside `tutorial/`:

1. **Set up environment and install deps**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate   # Windows

   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Configure your API key**

   - Copy `.env.example` to `.env` and fill in `OPENAI_API_KEY`.

3. **Run the end-to-end pipeline**

   ```bash
   python run_pipeline.py
   ```

   This will:

   - Load `data/input.csv`
   - Clean and transform text
   - Call the OpenAI API to generate summaries
   - Run basic quality checks
   - Save a timestamped CSV into `output/`

4. **Optional sanity check only**

   ```bash
   python src/test_openai.py
   ```

## How this maps to the tutorial

- **Step 3 (Setup & environment)** – matches the project layout and `requirements.txt` here.
- **Step 4 (Data ingestion)** – `src/ingest.py` and `data/input.csv`.
- **Step 5 (Data transformation)** – `src/transform.py`.
- **Step 6 (Prompting & AI processing)** – `src/generate.py` and `src/process.py`.
- **Step 7 (Evaluation & quality control)** – `src/evaluate.py` and `evaluate_outputs()` in `src/process.py`.
- **Step 8 (Persisting results)** – `src/save.py` and the `output/` / `logs/` folders.
- **Step 9–10 (Automation & packaging)** – `run_pipeline.py`, `requirements.txt`, and the overall structure.