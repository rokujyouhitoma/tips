all:
	python setup.py build_ext --inplace

test: all
	python test_run_4_cython.py

clean:
	@echo Cleaning
	@rm -f *.pyc blesenhamLine.c *.o *.so *~ core
	@rm -rf build
