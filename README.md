# PDF Ingestion with Docling

This project processes PDF files using Docling for ingestion tasks.

## Setup
- Install dependencies: `pip install docling` (assuming Docling is the library; adjust if it's a specific one like IBM's Docling).

## Usage
- Place PDFs in `data/`.
- Run the script in `src/`.

## Data
- PDFs are stored in `data/`. Example files: file1.pdf, file2.pdf.

## Running the Ingestion Script
- Place one or more PDF files in the `data/` directory.
- Activate the virtual environment: `source venv/bin/activate` (or equivalent).
- Run: `python src/ingest.py`
- The script will process each PDF one by one using Docling, export to JSON in `output/`, and log progress.
- Handles errors gracefully without stopping on failures.

## Steps
- More to come...