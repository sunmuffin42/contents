PYTHON := python

contents.in: contents_acq.py
	ls -R -o > contents.in
	$(PYTHON) contents_acq.py < contents.in > contents.out
	rm -f contents.in
	