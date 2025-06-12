"""Wrapper for FuseWill CLI using ``coaiapy`` utilities.

The ``coaiapy`` package provides ``coaiacli`` with a ``fuse`` command.
This wrapper delegates to that implementation while ensuring the
``coaiamodule`` helper can be imported alongside ``coaiacli``.
"""
import sys
import os

def main(argv=None):
    argv = argv or sys.argv[1:]
    try:
        from coaiapy import __file__ as coaiapy_path
        sys.path.append(os.path.dirname(coaiapy_path))
        from coaiapy import coaiacli
    except Exception as exc:
        raise SystemExit(f"Failed to load coaiapy fusewill: {exc}")
    sys.argv = ["coaia", "fuse", *argv]
    return coaiacli.main()

if __name__ == "__main__":
    main()
