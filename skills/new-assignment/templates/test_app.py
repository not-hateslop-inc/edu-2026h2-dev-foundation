from app import main


def test_returns_string():
    assert isinstance(main("테스트"), str)
