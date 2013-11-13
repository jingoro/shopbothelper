all: fetch-and-test

fetch-and-run: fetch run

fetch-and-test: fetch test

run:
	python shopbothelper.py

test:
	python test.py

fetch:
	@curl -s -o shopbothelper.py http://collabedit.com/download?id=eqef6
	@curl -s -o test.py http://collabedit.com/download?id=rp2u7
