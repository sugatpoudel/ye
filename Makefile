.PHONY: test build

test:
	pytest

build:
	python setup.py sdist bdist_wheel