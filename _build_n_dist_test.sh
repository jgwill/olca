rm -rf build/ dist/ *.egg-info **/*.egg-info &>/dev/null
python bump.py


# Including FuseWill in this distribution
src_dir="$(pwd)/olca"

python setup.py sdist bdist_wheel && (twine upload dist/* || pip install twine --quiet && twine upload dist/*)

