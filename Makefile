install:
	#install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	#format code
	black ./*.py ./**/*.py 
lint:
	#to check the code has proper syntax or not flake8 or pylint	
	pylint --disable=R,C ./*.py ./**/*.py 
test:
	#test where m is the marker and vv is the verbose with cov as coverage
	python -m pytest -vv --cov=main ./test_logic.py
build:
	#build container
deploy:
	#deploy
all: install lint test build deploy 