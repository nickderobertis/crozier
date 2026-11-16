

import pytest

from fern.types.xml_result import XmlResult


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlResult.from_xml("<result><header /><metadata /></result>")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlResult.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlResult.from_xml('<result dataUnknown="1"><Unknown a="1">v</Unknown></result>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlResult.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_preserves_child_order() -> None:
    parsed = XmlResult.from_xml("<result><header /><metadata /><header /></result>")
    assert "<header /><metadata /><header />" in parsed.to_xml(xml_declaration=False)


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlResult.from_xml("<NotTheresult />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlResult.from_xml("<result><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlResult.from_xml('<!DOCTYPE result [<!ENTITY xxe "injected">]><result>&xxe;</result>')
