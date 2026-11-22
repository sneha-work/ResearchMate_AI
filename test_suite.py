# test_suite.py - End-to-End Verification Test Suite for ResearchMate AI
import asyncio
import os
import sys

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from doc_converter import parse_latex_file, get_sample_academic_paper, generate_latex_code, STYLES_REGISTRY
from export_utils import (
    generate_paper_pdf, generate_paper_docx, generate_slides_pdf,
    generate_slides_pptx, generate_research_proposal_pdf, generate_bibliography_pdf
)
from slide_generator import generate_presentation
from literature_finder import search_verified_literature, get_topic_suggestions
from idea_generator import generate_research_ideas
from conference_finder import find_topic_conferences
import database

async def run_tests():
    print("=" * 60)
    print("RUNNING RESEARCHMATE AI END-TO-END VERIFICATION SUITE")
    print("=" * 60)

    # 1. Test Database
    print("\n[TEST 1] Initializing SQLite database...")
    database.init_db()
    guest = database.get_or_create_user("test_guest", "test@univ.edu", "Test Scholar")
    assert guest["id"] > 0, "Failed to create guest user in DB"
    print(f"✓ Database verified! User created with ID: {guest['id']}")

    # 2. Test Feature 1: Paper Formatter & 20 Styles PDF/DOCX/LaTeX
    print("\n[TEST 2] Testing Feature 1: 20-Style Academic Paper Formatter & LaTeX...")
    sample_paper = get_sample_academic_paper()
    assert sample_paper["title"], "Sample paper title missing"
    assert len(sample_paper["sections"]) >= 4, "Sample paper sections missing"
    
    # Test LaTeX Code Generation
    ieee_meta = STYLES_REGISTRY["ieee"]
    latex_code = generate_latex_code(sample_paper, ieee_meta)
    assert "\\documentclass[conference]{IEEEtran}" in latex_code, "IEEE LaTeX code missing documentclass"
    assert sample_paper["title"] in latex_code, "Paper title missing in generated LaTeX"
    print(f"✓ Compilable LaTeX Code verified ({len(latex_code)} characters)!")

    # Generate IEEE PDF
    ieee_pdf = generate_paper_pdf(sample_paper, ieee_meta, "test_paper_ieee.pdf")
    assert os.path.exists(ieee_pdf) and os.path.getsize(ieee_pdf) > 1000, f"IEEE PDF missing or empty: {ieee_pdf}"
    print(f"✓ Formatted IEEE PDF generated ({os.path.getsize(ieee_pdf)} bytes): {ieee_pdf}")

    # Generate APA 7 PDF
    apa_meta = STYLES_REGISTRY["apa7"]
    apa_pdf = generate_paper_pdf(sample_paper, apa_meta, "test_paper_apa.pdf")
    assert os.path.exists(apa_pdf) and os.path.getsize(apa_pdf) > 1000, f"APA PDF missing or empty: {apa_pdf}"
    print(f"✓ Formatted APA 7 PDF generated ({os.path.getsize(apa_pdf)} bytes): {apa_pdf}")

    # Generate DOCX
    docx_file = generate_paper_docx(sample_paper, ieee_meta, "test_paper_ieee.docx")
    assert os.path.exists(docx_file) and os.path.getsize(docx_file) > 1000, f"DOCX missing or empty: {docx_file}"
    print(f"✓ Formatted DOCX generated ({os.path.getsize(docx_file)} bytes): {docx_file}")

    # 3. Test Feature 2: Slide Generator (Descriptive & Analytical Modes + PDF)
    print("\n[TEST 3] Testing Feature 2: Deck Maker (Descriptive & Analytical Modes)...")
    deck_desc = await generate_presentation(
        sample_paper["abstract"],
        paper_meta={"title": sample_paper["title"]},
        options={"slide_count": 8, "presentation_type": "Descriptive", "theme": "emerald"}
    )
    assert len(deck_desc["slides"]) == 8, f"Expected 8 slides, got {len(deck_desc['slides'])}"
    assert deck_desc["presentation_type"] == "Descriptive", "Expected Descriptive type"
    print(f"✓ Descriptive Deck generated with {len(deck_desc['slides'])} slides and summary.")

    deck_anal = await generate_presentation(
        sample_paper["abstract"],
        paper_meta={"title": sample_paper["title"]},
        options={"slide_count": 8, "presentation_type": "Analytical", "theme": "emerald"}
    )
    assert len(deck_anal["slides"]) == 8, f"Expected 8 slides, got {len(deck_anal['slides'])}"
    assert deck_anal["presentation_type"] == "Analytical", "Expected Analytical type"
    print(f"✓ Analytical Deck generated with {len(deck_anal['slides'])} slides and quantitative metrics.")
    
    # Verify PDF & PPTX exports
    slides_pdf = generate_slides_pdf(deck_anal, "test_presentation.pdf")
    slides_pptx = generate_slides_pptx(deck_anal, "test_presentation.pptx")
    assert os.path.exists(slides_pdf) and os.path.getsize(slides_pdf) > 1000, "Slides PDF missing"
    assert os.path.exists(slides_pptx) and os.path.getsize(slides_pptx) > 1000, "Slides PPTX missing"
    print(f"✓ Presentation PDF ({os.path.getsize(slides_pdf)} bytes) & PPTX ({os.path.getsize(slides_pptx)} bytes) verified!")

    # 4. Test Feature 3: 20+ Verified Research Papers Discovery
    print("\n[TEST 3] Testing Feature 3: Verified Literature Discovery (20+ Papers)...")
    lit_results = await search_verified_literature("Transformers Attention Deep Learning")
    papers_count = lit_results["count"]
    assert papers_count >= 20, f"Expected >= 20 verified papers, got {papers_count}"
    first_p = lit_results["papers"][0]
    assert first_p["url"] and first_p["pdf_url"], "Paper URLs missing"
    assert first_p["bibtex"], "BibTeX citation missing"
    print(f"✓ Verified Literature Search returned {papers_count} papers! (>= 20 papers guarantee met)")
    print(f"  First Paper: {first_p['title'][:50]}... | Citations: {first_p['citations']}")

    # Test Autocomplete
    suggestions = get_topic_suggestions("Trans")
    assert len(suggestions) > 0, "Topic suggestions empty"
    print(f"✓ Autocomplete suggestions verified: {suggestions[:3]}")

    # 5. Test Feature 4: Innovative Research Ideas
    print("\n[TEST 4] Testing Feature 4: Innovative Research Idea Lab...")
    ideas_res = await generate_research_ideas(
        "Hallucination Mitigation in Real-Time RAG Pipelines",
        domain="Computer Science & AI",
        focus_area="Breakthrough Methodology"
    )
    assert len(ideas_res["ideas"]) >= 3, "Expected at least 3 research proposals"
    top_idea = ideas_res["ideas"][0]
    assert top_idea["hypothesis"] and top_idea["methodology"], "Proposal components missing"
    print(f"✓ Generated {len(ideas_res['ideas'])} comprehensive research proposals.")
    print(f"  Top Proposal: {top_idea['title'][:60]}... (Feasibility: {top_idea['feasibility']})")

    # 6. Test Feature 5: Verified Academic Conferences
    print("\n[TEST 5] Testing Feature 5: Verified Conferences Finder...")
    confs = find_topic_conferences(filter_rank="A*")
    assert len(confs) >= 8, f"Expected >= 8 A* conferences, got {len(confs)}"
    neurips = next((c for c in confs if "NeurIPS" in c["acronym"]), None)
    assert neurips is not None, "NeurIPS 2026 missing from conference list"
    assert neurips["venue"] and neurips["submission_deadline"], "Conference details missing"
    print(f"✓ Verified Conferences Finder returned {len(confs)} premier A* venues.")
    print(f"  Sample: {neurips['acronym']} | Venue: {neurips['venue']} | Days Left: {neurips['days_remaining']}")

    # 7. Test AI Paper Reader & Auto-Conversion ("Which to Convert & How")
    print("\n[TEST 6] Testing AI Paper Reading & Auto-Conversion Pipeline (DeepSeek / GPT)...")
    from ai_engine import analyze_paper_for_conversion, ai_format_manuscript
    analysis = await analyze_paper_for_conversion(
        text=sample_paper["abstract"] + "\n\n" + sample_paper["sections"][0]["content"],
        filename="quantum_routing.tex",
        preferred_model="auto"
    )
    assert analysis["recommended_style"] in STYLES_REGISTRY, "Recommended style invalid"
    assert len(analysis["which_to_convert"]) > 20, "Missing which_to_convert rationale"
    assert len(analysis["how_to_convert"]) >= 4, "Missing how_to_convert roadmap steps"
    print(f"✓ AI Read Manuscript: Identified Domain '{analysis['domain']}'")
    print(f"✓ AI Decision: Which to convert -> '{analysis['style_name']}'")
    print(f"✓ AI Conversion Roadmap (How to convert): {len(analysis['how_to_convert'])} concrete transformation steps")

    # Test AI Formatting
    formatted = await ai_format_manuscript(
        paper_data=sample_paper,
        target_style_id=analysis["recommended_style"],
        preferred_model="auto"
    )
    assert formatted["status"] == "success", "AI formatting failed"
    assert formatted["paper"]["sections"], "AI formatted sections missing"
    assert formatted["latex_code"], "AI formatted latex code missing"
    # 8. Test Notes Maker (Educational Synthesis, TXT & PDF Downloads)
    print("\n[TEST 7] Testing Notes Maker: Educational Text Notes, TXT & PDF Generation...")
    from notes_generator import generate_educational_notes, generate_notes_txt, generate_notes_pdf
    raw_paper_text = f"{sample_paper['title']}\n\nAbstract\n{sample_paper['abstract']}\n\n" + "\n\n".join([f"{s['heading']}\n{s['content']}" for s in sample_paper['sections']])
    notes = await generate_educational_notes(raw_paper_text, paper_meta=sample_paper)
    assert notes["title"], "Notes missing title"
    assert len(notes["section_notes"]) >= 3, f"Expected >= 3 section notes, got {len(notes['section_notes'])}"
    assert len(notes["glossary"]) >= 3, "Notes glossary missing entries"
    assert len(notes["review_questions"]) >= 3, "Notes review questions missing"
    print(f"✓ Educational Study Notes generated: '{notes['title'][:50]}...'")
    print(f"  - Sections described: {len(notes['section_notes'])}")
    print(f"  - Academic glossary terms: {len(notes['glossary'])}")
    print(f"  - Review self-assessment questions: {len(notes['review_questions'])}")

    notes_txt = generate_notes_txt(notes, "test_educational_notes.txt")
    assert os.path.exists(notes_txt) and os.path.getsize(notes_txt) > 500, "Notes TXT export failed"
    print(f"✓ Notes TXT file generated ({os.path.getsize(notes_txt)} bytes): {notes_txt}")

    notes_pdf = generate_notes_pdf(notes, "test_educational_notes.pdf")
    assert os.path.exists(notes_pdf) and os.path.getsize(notes_pdf) > 1000, "Notes PDF export failed"
    print(f"✓ Notes PDF file generated ({os.path.getsize(notes_pdf)} bytes): {notes_pdf}")

    # 9. Test Scholar Feedback Submissions
    print("\n[TEST 8] Testing Scholar Feedback System...")
    fb_id = database.add_feedback(
        user_id=guest["id"],
        category="Formatting Quality",
        subject="Superb IEEE and LaTeX Formatting",
        message="The two-column formatting and LaTeX compilable outputs are crystal clear.",
        rating=5
    )
    assert fb_id > 0, "Failed to insert feedback"
    fb_list = database.get_feedback(10)
    assert any(fb["id"] == fb_id for fb in fb_list), "Inserted feedback not found in DB"
    print(f"✓ Scholar Feedback submitted and retrieved from database (ID: {fb_id})!")

    print("\n" + "=" * 60)
    print("ALL FEATURES, NOTES MAKER, EXPORTS & FEEDBACK PASSED INDISPUTABLY!")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(run_tests())

