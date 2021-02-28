PYTHON := python

contents: contents_acq.py
	ls -R -o > contents
	$(PYTHON) contents_acq.py < contents > contents.out
	rm -f contents

catalog: catalog_traversal.py
	$(PYTHON) catalog_traversal.py > catalog.out