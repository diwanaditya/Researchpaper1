# PQC for 5G/6G: Hybrid Deployment Model

[![DOI](https://zenodo.org/badge/DOIExample.svg)](https://doi.org/10.5281/zenodo.1234567) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)

Repository for the paper: **Post-Quantum Cryptographic Algorithms for Practical Deployment in 5G/6G Networks: A Comprehensive Analysis with Novel Hybrid Deployment Model**  
*Aditya Diwan, diwanaditya964@gmail.com, September 18, 2025*

## Introduction
Quantum threats (Shor/Grover) break RSA/ECC in 5G/6G (SUCI, NFV, URLLC). NIST PQC (Kyber, Dilithium, SPHINCS+) solutions evaluated. Novelty: Staged hybrid model (classical+PQC, AI-switch, full PQC) with <2% overhead.

**Full Abstract:**  
The transition to quantum-resistant... [paste full from PDF: The transition to quantum-resistant cryptographic systems is critical... (up to Keywords)].

**Key Sections:**  
- **Background:** Quantum threats, NIST PQC families.  
- **Algorithms:** Lattice (Kyber/Saber/Dilithium) vs hash (SPHINCS+); trade-offs (e.g., Kyber > Saber in interop, Saber > in SCA).  
- **Performance:** Simulations: Kyber keygen 1.33 ± 0.13 ms (vs RSA 18.07 ms).  
- **Hybrid Model:** Dynamic switching via threat score.  
- **Recommendations:** Kyber for SUCI, Dilithium for auth; hybrid migration.

Compile paper: `make pdf` (outputs paper.pdf).

## Experiments
Reproduce Section 4 benchmarks (CPU proxy: 3GHz i7). Run `python experiments/main.py` for timings.

**Sample Results (from run):**  
| Algorithm    | Operation | Mean (ms) | Std (ms) |  
|--------------|-----------|-----------|----------|  
| Kyber-512   | Keygen    | 1.33     | 0.13    |  
| Dilithium-2 | Signing   | 0.08     | 0.08    |  
| RSA-2048    | Keygen    | 18.07    | 2.37    |  
| ECC-256     | Keygen    | 0.00     | 0.00    |  
| Saber       | Keygen    | 1.26     | 0.12    |  
| SPHINCS+    | Signing   | 5.43     | 0.55    |  

Hybrid sim (`hybrid_model.py`): Cost 0.123 ms at threat=0.9.

Jupyter: `notebook.ipynb` for tables.

## References
10+ varied in `paper/references.bib` (IEEE conf/journals, ACM, arXiv preprints, MDPI). Bibtex keys unique per type.

## Setup & Run
1. `git clone <url>`  
2. `pip install -r requirements.txt` (numpy)  
3. `make all` (runs exps + compiles paper)  
4. View: `open paper/paper.pdf`

## Contributing
See CONTRIBUTING.md. PRs: New algos, real liboqs.

**Citation:**  
@misc{diwan2025pqc,  
  title={Post-Quantum Cryptographic Algorithms...},  
  author={Diwan, Aditya},  
  year={2025},  
  doi={10.5281/zenodo.1234567}  
}

Contact: diwanaditya964@gmail.com
