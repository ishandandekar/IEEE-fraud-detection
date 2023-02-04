install:
	python -m pip install requirements.txt

format:
	black src/

data:
	python src/data/make_dataset.py