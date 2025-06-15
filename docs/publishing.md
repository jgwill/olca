# Publishing the Package

This guide explains how to package and upload `olca` to PyPI. Use TestPyPI first to avoid accidental public releases.

## Build the distributions

Install build and twine if you don't have them:
```bash
pip install build twine
```
Create the source distribution and wheel:
```bash
python -m build
```
The files will appear in the `dist/` folder.

## Upload to TestPyPI

Set your credentials as environment variables:
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=<your test PyPI token>
```
Upload the files:
```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
Verify installation with:
```bash
pip install --index-url https://test.pypi.org/simple/ olca --no-deps
```
Once everything looks good you can repeat the upload step without the `--repository-url` flag to publish to the real PyPI.
