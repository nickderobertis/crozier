

import pytest

from fern.types.xml_funder import XmlFunder


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlFunder.from_xml("<funder />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlFunder.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlFunder.from_xml('<funder dataUnknown="1"><Unknown a="1">v</Unknown></funder>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlFunder.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlFunder.from_xml("<NotThefunder />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlFunder.from_xml("<funder><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlFunder.from_xml('<!DOCTYPE funder [<!ENTITY xxe "injected">]><funder>&xxe;</funder>')
