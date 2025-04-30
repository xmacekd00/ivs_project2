.PHONY: all  pack clean test doc run profile

.DEFAULT_GOAL := all

all:
	@python3 calculator.py
pack: clean doc
	cd .. && mkdir -p repo
	cd .. && mkdir -p install
	cd .. && cp -r calc_installer  install/
	cd .. && cp -r stddev_installer  install/
	cd .. && cp -r .git repo/
	cd .. && cp -r src repo/
	cd .. && cp -r mockup repo/
	cd .. && cp -r plan repo/
	cd .. && cp -r profiling repo/
	cd .. && cp debugging.png repo/
	cd .. && cp dokumentace.pdf repo/
	cd .. && cp screenshot.png repo/ 
	cd .. && cp skutecnost.txt repo/
	cd .. && cp LICENSE.md repo/
	cd .. && cp hodnoceni.txt repo/
	cd .. && cp README.md repo/
	cd .. && cp .gitignore repo/
	cd .. && cp .editorconfig repo/
	cd .. && mkdir xmacekd00_xperuta00_xkrystm00_xcapkad00
	cd .. && cp -r doc repo install xmacekd00_xperuta00_xkrystm00_xcapkad00/
	cd .. && zip -r xmacekd00_xperuta00_xkrystm00_xcapkad00.zip xmacekd00_xperuta00_xkrystm00_xcapkad00
	cd .. && rm -rf xmacekd00_xperuta00_xkrystm00_xcapkad00
	cd .. && rm -rf doc
	cd .. && rm -rf install
	cd .. && rm -rf repo


clean:
	rm -rf "__pycache__"
	rm -rf "../doc"
	rm -rf ../*.zip
test:
	@python3 tdd.py
doc: Doxyfile
	doxygen Doxyfile
run:
	@python3	calculator.py
profile:
	@python3 stddev.py < stddev_sample_data.txt






