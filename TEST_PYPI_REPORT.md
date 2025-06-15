## Test PyPI Upload Report

Date: 2025-06-15 15:13:43 UTC

Steps:
1. Installed build and twine.
2. Ran `python -m build` to create source and wheel in `dist/`.
3. Exported credentials using `set -a && source $HOME/.env && set +a`.
4. Executed `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`.

Observed output:
```
Uploading distributions to https://test.pypi.org/legacy/
Uploading olca-0.3.2-py3-none-any.whl
WARNING  Error during upload. Retry with the --verbose option for more details.
ERROR    HTTPError: 400 Bad Request from https://test.pypi.org/legacy/
         Bad Request
```

The upload failed with HTTP 400, even after sourcing credentials from `.env`.
