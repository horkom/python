import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


def test_capitalize_positive(utils):
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("123") == "123"
    assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"


def test_capitalize_negative(utils):
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    with pytest.raises(AttributeError):
        utils.capitalize(None)


def test_trim_positive(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro") == "skypro"
    assert utils.trim("  skypro  ") == "skypro  "


def test_trim_negative(utils):
    assert utils.trim("") == ""
    assert utils.trim("   ") == ""
    with pytest.raises(AttributeError):
        utils.trim(None)


def test_contains_positive(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("123", "2") is True


def test_contains_negative(utils):
    assert utils.contains("", "a") is False
    assert utils.contains(" ", " ") is True
    with pytest.raises(AttributeError):
        utils.contains(None, "a")
    assert utils.contains("abc", "") is True


def test_delete_symbol_positive(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("123123", "1") == "2323"


def test_delete_symbol_negative(utils):
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol(" ", " ") == ""
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
    assert utils.delete_symbol("abc", "") == "abc"
