.DEFAULT_GOAL := all

all: calculator.py
	@python3 calculator.py 
pack:
	#prikaz pro udelani zipu
clean:
	rm -rf "__pycache__"
	rm -rf "../docs"
test:
	@python3 tdd.py
doc: Doxyfile
	doxygen Doxyfile
run:
	@python3	calculator.py
profile:
	@python3 stddev.py < stddev_sample_data.txt





