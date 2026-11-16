

import pytest

from fern.types.xml_response import XmlResponse


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlResponse.from_xml("<response><header /><results /></response>")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlResponse.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlResponse.from_xml('<response dataUnknown="1"><Unknown a="1">v</Unknown></response>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlResponse.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_preserves_child_order() -> None:
    parsed = XmlResponse.from_xml("<response><header /><results /><header /></response>")
    assert "<header /><results /><header />" in parsed.to_xml(xml_declaration=False)


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlResponse.from_xml("<NotTheresponse />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlResponse.from_xml("<response><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlResponse.from_xml('<!DOCTYPE response [<!ENTITY xxe "injected">]><response>&xxe;</response>')
