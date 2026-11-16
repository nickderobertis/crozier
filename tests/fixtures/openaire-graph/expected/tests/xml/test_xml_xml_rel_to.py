

import pytest

from fern.types.xml_rel_to import XmlRelTo


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlRelTo.from_xml("<to />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlRelTo.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlRelTo.from_xml('<to dataUnknown="1"><Unknown a="1">v</Unknown></to>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlRelTo.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlRelTo.from_xml("<NotTheto />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlRelTo.from_xml("<to><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlRelTo.from_xml('<!DOCTYPE to [<!ENTITY xxe "injected">]><to>&xxe;</to>')
