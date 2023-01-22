test:
	pytest -v --cov-config .coveragerc --cov=library_python -l --tb=short --maxfail=1 tests/
	coverage xml
	coverage html

build:
	python setup.py sdist bdist_wheel
