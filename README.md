**Censorship Circumvention & Internet Freedom: A Practical Guide to Research**

Author: Aditya Diwan
Repo Purpose: This repository is an educational template — it explains how to do research (design experiments, run safe simulations, draft papers, create reproducible artifacts) using censorship circumvention as an example topic.

⚠️ *Important: This repo does **NOT** contain or promote active probing of third-party networks. It provides templates, checklists, example documents, and safe simulated experiments only.*

---

#Quick Summary

A step-by-step, copy-pasteable teaching repo that helps students learn how to conduct safe, reproducible, and ethical research — using **censorship circumvention** as an illustrative case.

---

#Why This Repo Exists

Many students know programming but don’t know how to structure **research end-to-end**. This repo shows the **full research pipeline**:

* Pick a focused question
* Build a safe experimental plan
* Collect and sanitize data
* Analyze and plot results
* Write a paper & make reproducible artifacts public — all while following **ethical rules**

It’s intentionally **non-invasive**: all examples either simulate censorship locally or use sanitized public datasets. The repo is a **teaching resource**, not an operational toolkit for evasion.

---

#What This Repo Contains (Educational Artifacts)

```
/paper/                 # Paper skeleton and example paragraphs (LaTeX & Markdown)
    /main.tex
    /bibliography.bib

/docs/
    /SCOPE_TEMPLATE.md       # Project scope template
    /ETHICS_TEMPLATE.md      # Ethics statement template
    /PROJECT_BOARD.md        # Milestones & day-by-day plan
    /LIT_MATRIX_TEMPLATE.csv # Literature-review matrix (authors, year, method, gap)
    /SURVEY_TEMPLATE.md      # MCQ-only survey template (anonymous-safe)
    /READING_LIST.md         # Curated reading list + how to read papers

/examples/
    /SIMULATION_GUIDE.md     # How to simulate censorship locally (safe)
    /SAMPLE_RESULTS.csv      # Example sanitized results (for practice)
    /PLOTS_EXAMPLES.ipynb    # Jupyter notebook showing analysis + plots

/templates/
    /README_PROJECT.md       # Template for any research README
    /EMAIL_OUTREACH.txt      # Outreach email templates for professors
    /CV_BLURB.txt            # SOP/CV sample lines to include paper/repo
```

---

#How To Use This Repo (3 Quick Steps)

1. Clone the repo**
```
git clone https://github.com/YourUsername/circumvention-research.git
cd circumvention-research
```
2. Read the teaching docs**
   * Start with `docs/SCOPE_TEMPLATE.md` → learn how to scope a project.
   * Read `docs/ETHICS_TEMPLATE.md` → understand safety & what not to do.
   * Open `examples/SIMULATION_GUIDE.md` → run local, safe simulations.
3. Follow the Day-by-Day Plan**
   * `docs/PROJECT_BOARD.md` → step-by-step tasks (Day 1 → Day 8).
   * Use `/templates/` to produce artifacts (paper, survey, logs).

---

# What You Will Learn (Outcomes)

How to convert an idea into a **scoped research question**
How to build a **safe experimental setup** (simulation-first)
How to do a **literature review** (with `LIT_MATRIX_TEMPLATE.csv`)
How to collect, sanitize & present **reproducible results**
How to write a **publishable paper** (LaTeX skeleton included)
How to package research artifacts for **admissions & reviewers** (arXiv + GitHub + README)



Strong Safety & Ethics Reminder

This repo **intentionally avoids** instructions that involve interacting with unknown third-party networks or targeting live censorship infrastructure.

If you expand beyond simulation/public datasets:

* Obtain explicit permission from network owners.
* Get IRB/ethics approval for human-subject research.
* Never distribute raw logs with sensitive info.
* Always include a clear **Ethics Statement** in public write-ups.

Suggested ethics snippet :

> All active experiments were performed on infrastructure controlled by the researchers or on cloud instances explicitly provisioned for the study. No experiments probed or interfered with third-party networks. All survey instruments were anonymous and collected no personally identifying information.


Example Workflow (Compact)

1. Fill `docs/SCOPE_TEMPLATE.md` → commit
2. Populate `docs/LIT_MATRIX_TEMPLATE.csv` with \~20 papers
3. Run local simulation (see `examples/SIMULATION_GUIDE.md`)
4. Save results in `examples/SAMPLE_RESULTS.csv`
5. Analyze in `examples/PLOTS_EXAMPLES.ipynb`
6. Draft paper in `paper/main.tex` with figures/tables
7. Release on GitHub + upload preprint to **arXiv/Zenodo**
8. Add one-page summary in `templates/README_PROJECT.md`

