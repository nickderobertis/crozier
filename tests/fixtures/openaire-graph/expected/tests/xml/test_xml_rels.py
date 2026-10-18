

import pytest

from fern.types.xml_rels import XmlRels


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlRels.from_xml("<rels><rel /></rels>")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlRels.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlRels.from_xml('<rels dataUnknown="1"><Unknown a="1">v</Unknown></rels>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlRels.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlRels.from_xml("<NotTherels />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlRels.from_xml("<rels><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlRels.from_xml('<!DOCTYPE rels [<!ENTITY xxe "injected">]><rels>&xxe;</rels>')
