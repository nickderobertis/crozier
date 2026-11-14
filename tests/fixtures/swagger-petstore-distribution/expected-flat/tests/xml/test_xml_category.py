

import pytest
from acme.types.category import Category


def test_from_xml_to_xml_round_trips() -> None:
    parsed = Category.from_xml("<category />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert Category.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = Category.from_xml('<category dataUnknown="1"><Unknown a="1">v</Unknown></category>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert Category.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        Category.from_xml("<NotThecategory />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        Category.from_xml("<category><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        Category.from_xml('<!DOCTYPE category [<!ENTITY xxe "injected">]><category>&xxe;</category>')
