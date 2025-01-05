lint:
	flake8 .
test:
	python -m unittest discover -s tests -p "*.py
	
all: lint test