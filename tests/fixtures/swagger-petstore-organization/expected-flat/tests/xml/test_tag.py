

import pytest
from PetStore.types.tag import Tag


def test_from_xml_to_xml_round_trips() -> None:
    parsed = Tag.from_xml("<tag />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert Tag.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = Tag.from_xml('<tag dataUnknown="1"><Unknown a="1">v</Unknown></tag>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert Tag.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        Tag.from_xml("<NotThetag />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        Tag.from_xml("<tag><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        Tag.from_xml('<!DOCTYPE tag [<!ENTITY xxe "injected">]><tag>&xxe;</tag>')
