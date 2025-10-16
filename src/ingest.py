import os
from docling.document_converter import DocumentConverter

# Define directories relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', 'data')
output_dir = os.path.join(script_dir, '..', 'output')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

def process_pdfs():
    converter = DocumentConverter()
    
    # Get list of PDF files
    pdf_files = [f for f in os.listdir(data_dir) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the data directory.")
        return
    
    for pdf_file in pdf_files:
        source_path = os.path.join(data_dir, pdf_file)
        try:
            conv_result = converter.convert(source_path)
            # Export to JSON
            output_path = os.path.join(output_dir, pdf_file.replace('.pdf', '.json'))
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(conv_result.document.export_to_markdown())
            print(f"Successfully processed {pdf_file} and saved to {output_path}")
        except Exception as e:
            print(f"Error processing {pdf_file}: {str(e)}")
            # Continue to next file instead of stopping

if __name__ == "__main__":
    process_pdfs()