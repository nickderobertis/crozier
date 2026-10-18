

import pytest

from fern.types.xml_rel import XmlRel


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlRel.from_xml("<rel><to /><country /></rel>")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlRel.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlRel.from_xml('<rel dataUnknown="1"><Unknown a="1">v</Unknown></rel>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlRel.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_preserves_child_order() -> None:
    parsed = XmlRel.from_xml("<rel><to /><country /><to /></rel>")
    assert "<to /><country /><to />" in parsed.to_xml(xml_declaration=False)


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlRel.from_xml("<NotTherel />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlRel.from_xml("<rel><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlRel.from_xml('<!DOCTYPE rel [<!ENTITY xxe "injected">]><rel>&xxe;</rel>')
