test:
	make install
	pytest -v --cov-config .coveragerc --cov=library_python -l --tb=short --maxfail=1 tests/
	coverage xml
	coverage html
	make uninstall

install:
	pip install -e .

install-requirements:
	pipenv install

lint:
	pylint sample_project

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf build dist sample_project.egg-info

docs:
	sphinx-build -b html docs docs/build

uninstall:
	pip uninstall sample_project

shell:
	pipenv shell