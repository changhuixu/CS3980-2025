# this file shows how to test Exceptions

import pytest


def f():
    raise SystemExit(1)


def test_verify_exception():
    with pytest.raises(SystemExit):
        f()
