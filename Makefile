all:	fetch run

run:
	python shopbothelper.py

fetch:
	curl -o shopbothelper.py http://collabedit.com/download?id=eqef6 
