import fitz  # PyMuPDF
import requests
import os
import pandas as pd

def download_pdf(pdf_url, save_path):
    """
    Download a PDF from a URL and save it locally.
    """
    response = requests.get(pdf_url)
    with open(save_path, 'wb') as pdf_file:
        pdf_file.write(response.content)
    print(f"Downloaded PDF to {save_path}")

def analyze_pdf(file_path):
    """
    Analyze a PDF and extract information about elements on the page.
    """
    try:
        pdf_document = fitz.open(file_path)
        print(f"Opened PDF: {file_path}")

        analysis_results = []
        
        # Iterate through each page
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            print(f"Analyzing Page {page_number + 1}...")

            # Get text and layout info
            text = page.get_text("dict")  # Extract text as a dictionary with layout details
            for block in text["blocks"]:
                block_coords = block["bbox"]  # Get bounding box of the block (x0, y0, x1, y1)
                block_text = block.get("lines", [{}])[0].get("spans", [{}])[0].get("text", "")
                print(f"Block at {block_coords}: {block_text}")

                # Example: Add analysis result
                analysis_results.append({
                    "Page": page_number + 1,
                    "Block Text": block_text,
                    "Coordinates": block_coords
                })

        pdf_document.close()
        return analysis_results

    except Exception as e:
        print(f"Error analyzing PDF: {e}")
        return []

def save_to_excel(data, output_file):
    """
    Save analysis results to an Excel file.
    """
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False, engine="openpyxl")
    print(f"Results saved to {output_file}")

# Example Usage
pdf_url = "https://pixika2-live.s3.ap-south-1.amazonaws.com/Alkem_Laboratories_Ltd_Alkem_Hr_DIY_Calendar_A5_1421/SLOT01/MUMB/mumb-016.diycalendar.pdf?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAUPELPOQIYUS5UWFT%2F20250102%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20250102T065747Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=f4c77d482b9d08cbb45f9ca271eb4c1ce0b519288503e6424356abe2fa093371"
# Replace with your PDF link
pdf_file_path = "sample_calendar.pdf"
output_excel = "pdf_analysis_results.xlsx"

# Step 1: Download the PDF
download_pdf(pdf_url, pdf_file_path)

# Step 2: Analyze the PDF
results = analyze_pdf(pdf_file_path)

# Step 3: Save results to Excel
if results:
    save_to_excel(results, output_excel)
