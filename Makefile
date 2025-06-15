.PHONY: bump_version clean dist publish test-release

bump_version:
	python bump.py

clean:
	rm -rf build/ dist/ *.egg-info **/*.egg-info
	@rm -rf build dist *.egg-info 2>/dev/null || true

dist: clean
	python -m build

publish: dist
	twine upload dist*

test-release: clean
	python -m pytest -q
	pip install build twine --quiet
	python -m build
	twine upload --repository testpypi dist/*
