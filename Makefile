install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	#force install latest whisper
	#pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

test:
	python -m pytest -vv test_*.py

format:	
	black *.py
	#black *.py hugging-face/zero_shot_classification.py hugging-face/hf_whisper.py

lint:
	pylint --disable=R,C *.py
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py\
	#	 hugging-face/zero_shot_classification.py hugging-face/hf_whisper.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install format lint test