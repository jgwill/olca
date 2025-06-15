rm -rf build/ dist/ *.egg-info **/*.egg-info &>/dev/null
python bump.py

python setup.py sdist bdist_wheel && (twine upload dist/* || pip install twine --quiet && twine upload dist/*)

