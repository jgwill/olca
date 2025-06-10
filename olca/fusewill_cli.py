"""Wrapper for FuseWill CLI using coaiapy.cofuse."""
import sys

def main(argv=None):
    argv = argv or sys.argv[1:]
    try:
        from coaiapy.cofuse import main as coaia_main
    except Exception as exc:
        raise SystemExit(f"Failed to load coaiapy fusewill: {exc}")
    coaia_main(argv)

if __name__ == "__main__":
    main()
