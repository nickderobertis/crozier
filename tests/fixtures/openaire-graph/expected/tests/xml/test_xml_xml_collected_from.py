

import pytest

from fern.types.xml_collected_from import XmlCollectedFrom


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlCollectedFrom.from_xml("<collectedfrom />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlCollectedFrom.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlCollectedFrom.from_xml('<collectedfrom dataUnknown="1"><Unknown a="1">v</Unknown></collectedfrom>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlCollectedFrom.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlCollectedFrom.from_xml("<NotThecollectedfrom />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlCollectedFrom.from_xml("<collectedfrom><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlCollectedFrom.from_xml(
            '<!DOCTYPE collectedfrom [<!ENTITY xxe "injected">]><collectedfrom>&xxe;</collectedfrom>'
        )
