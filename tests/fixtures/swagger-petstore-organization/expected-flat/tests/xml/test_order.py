

import pytest
from PetStore.types.order import Order


def test_from_xml_to_xml_round_trips() -> None:
    parsed = Order.from_xml("<order />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert Order.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = Order.from_xml('<order dataUnknown="1"><Unknown a="1">v</Unknown></order>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert Order.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        Order.from_xml("<NotTheorder />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        Order.from_xml("<order><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        Order.from_xml('<!DOCTYPE order [<!ENTITY xxe "injected">]><order>&xxe;</order>')
