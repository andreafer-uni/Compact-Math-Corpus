import spacy

nlp = spacy.load("en_core_web_sm")

def is_noun_noun(phrase):
    doc = nlp(phrase)
    return len(doc) == 2 and all(token.pos_ == "NOUN" for token in doc)

def load_terms(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip().lower() for line in file if line.strip()]

def filter_noun_noun(terms):
    return [term for term in terms if is_noun_noun(term)]

def compare_lists(tex_file, pdf_file):
    tex_terms = load_terms(tex_file)
    pdf_terms = load_terms(pdf_file)

    tex_nns = set(filter_noun_noun(tex_terms))
    pdf_nns = set(filter_noun_noun(pdf_terms))

    return {
        "tex_total": len(tex_nns),
        "pdf_total": len(pdf_nns),
        "shared": len(tex_nns & pdf_nns),
        "only_tex": len(tex_nns - pdf_nns),
        "only_pdf": len(pdf_nns - tex_nns),
        "examples": {
            "shared": list(tex_nns & pdf_nns)[:10],
            "only_tex": list(tex_nns - pdf_nns)[:10],
            "only_pdf": list(pdf_nns - tex_nns)[:10]
        }
    }
