# ResearchMate AI — Academic Research & Publication Suite

## 🌐 Live Website
- **Website URL**: https://researchmate-ai-scyd.onrender.com/

---

## 🎨 Color Palette & Design System

ResearchMate AI features an elegant, eye-friendly academic design system:

| Color Name | Hex Code | Visual Preview / Role |
| :--- | :--- | :--- |
| **Ivory Cream** | `#F2EBDD` | Primary app background (light mode) providing warm paper-like contrast |
| **Sage Green** | `#78947F` | Subtle borders, dividers, secondary tags, and muted icons |
| **Emerald Accent** | `#185844` | Primary brand color, primary action buttons, and active tabs |
| **Deep Forest** | `#102F27` | High-contrast body text (light mode) and primary dark background |
| **Antique Gold** | `#B08A4F` | Academic milestone badges, highlights, and dark-mode accent buttons |
| **Pure White** | `#FFFFFF` | Card surface and editor canvas (light mode) |
| **Forest Night** | `#153B32` | Elevated card container surface (dark mode) |

- **Typography**: 
  - Headings: `Outfit` & `Plus Jakarta Sans`
  - Body: Modern System UI Font Stack
  - Editorial & Mathematical Content: `Merriweather` / Standard Serif
- **Themes**: Seamless 1-click toggle between Light Mode and Dark Mode.

---

## 📖 About The Website

**ResearchMate AI** is an all-in-one academic companion built for students, university scholars, professors, and researchers. It automates tedious research workflows, manuscript formatting, literature discovery, and study material synthesis into a clean, modern interface.

### 5 Core Features:

### 1. 20-Style Academic Paper Formatter (`/formatter`)
- **Document Input**: Upload Microsoft Word (`.docx`), LaTeX (`.tex`), Plain Text (`.txt`), or paste raw manuscript text.
- **20 Global Publication Styles**: IEEE Conference/Transactions, ACM (sigconf), APA 7th Edition, Harvard Referencing, Springer LNCS, Nature, Elsevier (ScienceDirect), MLA 9th Edition, Chicago Manual of Style, Cell Press, Oxford Academic, MDPI, AIP, Frontiers, PLOS ONE, Wiley, Taylor & Francis, Cambridge University Press, and Emerald.
- **Live Dual-Pane Editor**: Real-time side-by-side preview matching standard two-column or single-column journal formatting.
- **Direct Downloads**:
  - Publication-grade **PDF**
  - Native Microsoft Word **DOCX**
  - Standard LaTeX source code **.tex**

### 2. Descriptive Theory Notes Maker (`/notes`)
- **Document-Driven Analysis**: Upload any research paper or manuscript (PDF, DOCX, LaTeX, TXT) or paste text. Topics are extracted directly from the uploaded material.
- **Descriptive Theory Notes Structure**:
  - **Topic Title**: Extracted section and thematic headings
  - **Definition**: In-depth theoretical explanation of fundamental principles
  - **Main Layers / Key Components**: Numbered breakdown with detailed explanations
  - **Working**: Operational pipeline flow (`Input -> Processing -> Output`) with descriptive mechanism walkthrough
  - **Applications**: Real-world practical use cases and domain implementations
  - **Advantages**: Comprehensive breakdown of key benefits
  - **Summary of Topic**: Descriptive wrap-up summary paragraph
- **Direct Downloads**:
  - Download Full Theory Notes **PDF (`.pdf`)**
  - Download Plain Text Notes **TXT (`.txt`)**

### 3. Verified Literature Discovery (`/literature`)
- **Real-Time Academic Search**: Direct integration with arXiv API (`export.arxiv.org`) retrieving at least 20 verified peer-reviewed publications per query.
- **Verified Metadata**: Title, authors, publication year, summary, citation counts, DOI, direct paper link, and direct PDF download link.
- **1-Click BibTeX**: Instant modal to copy standardized BibTeX citations for your reference manager.

### 4. Innovative Research Idea Lab (`/ideas`)
- **Automated Research Proposals**: Formulates 3 distinct breakthrough proposals based on any inquiry domain.
- **Comprehensive Structure**: Novelty Hypothesis, Literature Gap analysis, Step-by-Step Methodology, Experimental Protocol (datasets, baselines, evaluation metrics), and Feasibility Score (1-10).
- **Direct Download**: Export complete research proposals as a formatted **PDF**.

### 5. Verified Conferences Tracker (`/conferences`)
- **Premier Academic Venues**: Tracks CORE A* and A international conferences across AI, Machine Learning, Systems, Security, and Computer Science (NeurIPS, ICML, CVPR, ICLR, ACL, KDD, IEEE S&P, OSDI, etc.).
- **Live Urgency Timers**: Dynamic countdown clocks displaying remaining days to submission deadlines.
- **Official Portals**: Direct links to Calls for Papers (CFP) and submission guidelines.

---

## 🛠️ Additional Platform Features
- **Scholar Feedback System (`/settings` & `/api/feedback`)**: Built-in feedback form with rating system and real-time submitted feedback viewer.
- **Profile & History**: Centralized dashboard to save papers, ideas, and review past formatted documents.
- **1-Click Guest & Scholar Sign-In**: Zero friction access with session preservation.

---

## 🚀 Running Locally

### 1. Requirements
- Python 3.10+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Launch the Application
```bash
python run.py
```
Open your browser to:
`http://localhost:8000`

### 3. Run Verification Tests
```bash
python test_suite.py
```
