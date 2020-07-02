import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True
#   pytest.xfail("This test should fail")

@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False