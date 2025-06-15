import importlib
import pytest


def test_fusewill_cli_loads():
    module = importlib.import_module('olca.fusewill_cli')
    with pytest.raises(SystemExit) as exc:
        module.main(['--help'])
    assert exc.value.code == 0
