import importlib
import pytest

pytest.importorskip("PIL", reason="Pillow required for CLI help")


def test_olca_help():
    module = importlib.import_module('olca.olcacli')
    with pytest.raises(SystemExit) as exc:
        module.main(['--help'])
    assert exc.value.code == 0
