Censorship Circumvention & Internet Freedom

Project: Censorship Circumvention & Internet Freedom: A Practical Guide to Research (Educational Template)
Author: Aditya Diwan
Repo purpose: This repository is an educational template — it explains how to do research (design experiments, run safe simulations, draft papers, create reproducible artifacts) using censorship circumvention as an example topic. This repo does NOT contain or promote active probing of third-party networks. It provides templates, checklists, example documents, and safe simulated experiments only.

Quick summary (one line)

A step-by-step, copy-pasteable teaching repo that helps students learn how to conduct safe, reproducible, and ethical research — using censorship circumvention as an illustrative case.

Why this repo exists

Many students know programming but don’t know how to structure research end-to-end. This repo shows the full research pipeline:

pick a focused question,

build a safe experimental plan,

collect and sanitize data,

analyze and plot results,

write a paper and make reproducible artifacts public — all while following ethical rules.

It’s intentionally non-invasive: all examples either simulate censorship locally or use sanitized public datasets. The repo is a teaching resource, not an operational toolkit for evasion.

What this repo contains (educational artifacts)
/paper/                 # Paper skeleton and example paragraphs (LaTeX & Markdown)
 /main.tex
 /bibliography.bib
/docs/
 /SCOPE_TEMPLATE.md     # Project scope template
 /ETHICS_TEMPLATE.md    # Ethics statement template
 /PROJECT_BOARD.md      # Milestones & day-by-day plan
 /LIT_MATRIX_TEMPLATE.csv # literature-review matrix (authors, year, method, gap)
 /SURVEY_TEMPLATE.md    # MCQ-only survey template (anonymous-safe)
 /READING_LIST.md       # Curated reading list + how to read papers
/examples/
 /SIMULATION_GUIDE.md   # How to simulate censorship locally (safe)
 /SAMPLE_RESULTS.csv    # Example sanitized results (for practice)
 /PLOTS_EXAMPLES.ipynb  # Jupyter notebook showing analysis + plots
/templates/
 /README_PROJECT.md     # Template for any research README
 /EMAIL_OUTREACH.txt    # Outreach email templates for professors
 /CV_BLURB.txt          # SOP/CV sample lines to include paper/repo

How to use this repo (3 quick steps)

Clone the repo

git clone https://github.com/YourUsername/circumvention-research.git
cd circumvention-research


Read the teaching docs

Start with docs/SCOPE_TEMPLATE.md to learn how to scope a project.

Read docs/ETHICS_TEMPLATE.md to understand safety and what not to do.

Open examples/SIMULATION_GUIDE.md to learn how to run local, safe simulations (no external scanning).

Follow the Day-by-Day plan

docs/PROJECT_BOARD.md contains step-by-step tasks (Day 1 → Day 8). Work through them and use the templates in /templates/ to produce artifacts (paper skeleton, survey, logs).

What you will learn (outcomes)

How to convert an idea into a well-scoped research question.

How to build a safe experimental setup (simulation-first).

How to do a literature review (use the LIT_MATRIX_TEMPLATE.csv).

How to collect, sanitize, and present reproducible results (CSV + Jupyter).

How to write a publishable paper (LaTeX skeleton + examples).

How to package research artifacts for admissions / reviewers (ArXiv + GitHub + README).

Strong safety & ethics reminder — read first

This repo intentionally avoids instructions that involve interacting with unknown third-party networks or targeting live censorship infrastructure. If you or collaborators plan to expand beyond simulation or public datasets:

Obtain explicit permission from network owners before scanning or probing.

Get IRB / ethics approval for human-subject research or collecting sensitive logs.

Never distribute raw logs containing identifying information.

Always include a clear Ethics statement in any public write-up.

Suggested ethics snippet (copy-paste for papers):

All active experiments were performed on infrastructure controlled by the researchers or on cloud instances explicitly provisioned for the study. No experiments probed or interfered with third-party networks. All survey instruments were anonymous and collected no personally identifying information.

Example workflow (compact)

Fill docs/SCOPE_TEMPLATE.md → commit.

Populate docs/LIT_MATRIX_TEMPLATE.csv with 20 papers (three-pass reading).

Use examples/SIMULATION_GUIDE.md to run a local simulated censorship test (only on your own VM). Generate examples/SAMPLE_RESULTS.csv (practice data is included).

Run analysis in examples/PLOTS_EXAMPLES.ipynb to create plots.

Draft paper/main.tex using the skeleton; insert figures/tables.

Make a GitHub release and upload a preprint to arXiv (or Zenodo for DOI). Add a one-page summary in README_PROJECT.md.

Ready-to-use copy-paste items (where to find them)

docs/SCOPE_TEMPLATE.md — scope checklist you must fill.

docs/ETHICS_TEMPLATE.md — ethics & consent language for your paper.

templates/README_PROJECT.md — boilerplate README you can reuse for any research repo.

templates/EMAIL_OUTREACH.txt — 1-paragraph outreach email templates for profs.

templates/CV_BLURB.txt — exact lines to paste into your CV/SOP about the repo/paper.
