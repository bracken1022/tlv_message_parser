all:
	python -m unittest discover -s test

clean:
	rm src/*.pyc
	rm test/*.pyc
