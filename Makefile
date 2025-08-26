# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD  ?= sphinx-build
SOURCEDIR    = .
BUILDDIR     = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Custom targets for course website
clean-notebooks:
	find . -name "*.ipynb" -exec jupyter nbconvert --clear-output --inplace {} \;

serve:
	cd _build/html && python -m http.server 8000

install-deps:
	pip install -r requirements.txt

build-course:
	make clean
	make html
	@echo "Course website built successfully!"
	@echo "Open _build/html/index.html in your browser"

watch:
	sphinx-autobuild . _build/html --ignore="*.ipynb_checkpoints*"

deploy-github:
	@echo "Deploying to GitHub Pages..."
	make html
	touch _build/html/.nojekyll
	@echo "Add _build/html/ contents to gh-pages branch"
