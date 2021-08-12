create-venv:
	python3 -m venv venv

install-requirements:
	pip install requirements.txt

remove-venv:
	rm -rf ./venv