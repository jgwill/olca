"""Wrapper for FuseWill CLI using ``coaiapy.cofuse``.

This adds the ``coaiapy`` package directory to ``sys.path`` so that
``coaiamodule`` (a sibling module required by ``cofuse``) can be imported
correctly.
"""
import sys
import os

def main(argv=None):
    argv = argv or sys.argv[1:]
    try:
        from coaiapy import __file__ as coaiapy_path
        sys.path.append(os.path.dirname(coaiapy_path))
        from coaiapy.cofuse import main as coaia_main
    except Exception as exc:
        raise SystemExit(f"Failed to load coaiapy fusewill: {exc}")
    coaia_main(argv)

if __name__ == "__main__":
    main()
