# Makefile
default: html

html:
	sphinx-build -b html -Ea source build/html

