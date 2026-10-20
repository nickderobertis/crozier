

import pytest

from fern.types.xml_provenance_action import XmlProvenanceAction


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlProvenanceAction.from_xml("<provenanceaction />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlProvenanceAction.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlProvenanceAction.from_xml(
        '<provenanceaction dataUnknown="1"><Unknown a="1">v</Unknown></provenanceaction>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlProvenanceAction.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlProvenanceAction.from_xml("<NotTheprovenanceaction />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlProvenanceAction.from_xml("<provenanceaction><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlProvenanceAction.from_xml(
            '<!DOCTYPE provenanceaction [<!ENTITY xxe "injected">]><provenanceaction>&xxe;</provenanceaction>'
        )
