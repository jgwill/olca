.PHONY: bump_version clean dist publish

bump_version:
	python bump.py

clean:
	rm -rf build/ dist/ *.egg-info **/*.egg-info
	@rm -rf build dist *.egg-info 2>/dev/null || true

dist: clean
	python -m build

publish: dist
	twine upload dist/*
