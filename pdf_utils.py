import fitz

def load_pdf(path: str):
    doc = fitz.open(path)
    text = "\n".join(page.get_text() for page in doc)
    return split_into_sections(text)

def split_into_sections(text: str):
    sections = {}
    current = "Introduction"
    sections[current] = ""

    for line in text.splitlines():
        if line.isupper() and len(line) < 60:
            current = line.strip()
            sections[current] = ""
        else:
            sections[current] += line + " "
    return sections