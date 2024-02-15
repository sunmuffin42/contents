PYTHON := python

DATE = $(shell date +'%Y%m%d')

# all:
#     $(PYTHON) catalog_traversal.py > "catalog_$(DATE).out"
contents: contents_acq.py
	ls -R -o > contents
	$(PYTHON) contents_acq.py < contents > "contents_$(DATE).out"
	rm -f contents

catalog: catalog_traversal.py
	$(PYTHON) catalog_traversal.py > "catalog_$(DATE).out"