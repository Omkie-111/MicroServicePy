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
	python -m pytest -vv --cov=main test_logic.py 
build:
	#build container
	docker build -t deploy-streamlit .
run:
	#run docker
	docker run -p 127.0.0.1:8501:8501 deploy-streamlit:latest
deploy:
	#deploy
all: install lint test build deploy 