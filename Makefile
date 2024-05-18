install:
	#install commands
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt
format:
	#format code
lint:
	#to check the code has proper syntax or not flake8 or pylint	
test:
	#test
deploy:
	#deploy
all: install lint test deploy 