

import pytest

from fern.types.xml_metadata import XmlMetadata


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlMetadata.from_xml('<metadata><entity xmlns="http://namespace.openaire.eu/oaf" /></metadata>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlMetadata.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlMetadata.from_xml('<metadata dataUnknown="1"><Unknown a="1">v</Unknown></metadata>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlMetadata.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlMetadata.from_xml("<NotThemetadata />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlMetadata.from_xml("<metadata><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlMetadata.from_xml('<!DOCTYPE metadata [<!ENTITY xxe "injected">]><metadata>&xxe;</metadata>')
