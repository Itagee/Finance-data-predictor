PYTHON = python3

test:
	$(PYTHON) -m unittest discover -s tests -p "*.py"

lint:
	flake8 .
