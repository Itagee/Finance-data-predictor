lint:
	flake8 .
test:
    $(PYTHON) -m unittest discover -s tests -p "*.py"
