import importlib
import pytest


def test_coaia_help():
    module = importlib.import_module('olca.coaia_cli')
    with pytest.raises(SystemExit) as exc:
        module.main(['--help'])
    assert exc.value.code == 0
