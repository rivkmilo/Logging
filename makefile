create-venv:
	python3 -m venv venv
	pip install requirements.txt

remove-venv:
	rm -rf ./venv