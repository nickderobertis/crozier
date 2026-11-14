

import pytest

from fern.types.xml_project import XmlProject


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlProject.from_xml(
        "<project><collectedfrom /><pid /><measure /><subject /><contracttype /><fundingtree /><datainfo /><rels /></project>"
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlProject.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlProject.from_xml('<project dataUnknown="1"><Unknown a="1">v</Unknown></project>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlProject.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_preserves_child_order() -> None:
    parsed = XmlProject.from_xml("<project><collectedfrom /><pid /><collectedfrom /></project>")
    assert "<collectedfrom /><pid /><collectedfrom />" in parsed.to_xml(xml_declaration=False)


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlProject.from_xml("<NotTheproject />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlProject.from_xml("<project><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlProject.from_xml('<!DOCTYPE project [<!ENTITY xxe "injected">]><project>&xxe;</project>')
