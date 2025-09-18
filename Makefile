all: experiments paper

experiments:
	cd experiments && python main.py && python hybrid_model.py
	cp experiments/results.md .

paper:
	cd paper && pdflatex paper.tex && bibtex paper && pdflatex paper.tex && pdflatex paper.tex

clean:
	rm -f *.aux *.bbl *.log *.pdf results.md
