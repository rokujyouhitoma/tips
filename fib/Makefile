build:
	python setup.py build_ext --inplace

test: build
	pep8 .
	python test.py
	python test_cython.py

clean:
	@echo Cleaning
	@rm -f *.pyc *.c *.o *.so *~ core
	@rm -rf build
