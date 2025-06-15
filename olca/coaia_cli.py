"""Wrapper for coaiapy CLI."""
import sys

def main(argv=None):
    argv = argv or sys.argv[1:]
    try:
        from coaiapy.coaiacli import main as coaia_main
    except Exception as exc:
        raise SystemExit(f"Failed to load coaiapy CLI: {exc}")
    sys.argv = ["coaia", *argv]
    coaia_main()

if __name__ == "__main__":
    main()
