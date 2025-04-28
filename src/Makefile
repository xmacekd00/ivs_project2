.PHONY: all  pack clean test doc run profile

.DEFAULT_GOAL := all

all:
	@python3 calculator.py
pack: clean
	cd .. && zip -r xmacekd00_xperuta00_xcapkad00_xkrystm00.zip . -x ".git/*" -x "installer/*"

clean:
	rm -rf "__pycache__"
	rm -rf "../doc"
test:
	@python3 tdd.py
doc: Doxyfile
	doxygen Doxyfile
run:
	@python3	calculator.py
profile:
	@python3 stddev.py < stddev_sample_data.txt






