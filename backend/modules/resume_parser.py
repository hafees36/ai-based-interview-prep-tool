import pdfplumber  

def extract_text_from_pdf(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:  # avoid NoneType errors
                    text += page_text + "\n"

    except Exception as e:
        print("Error reading PDF:", e)
        return None

    return text.strip()


if __name__ == "__main__":
    sample_file = "sample_resume.pdf"  # Put your resume file in same folder
    extracted_text = extract_text_from_pdf(sample_file)

    if extracted_text:
        print("===== Extracted Resume Text =====\n")
        print(extracted_text)
    else:
        print("No text extracted.")