install:
	python -m pip install -r requirements.txt

format:
	black src/

data:
	python src/data/make_dataset.py