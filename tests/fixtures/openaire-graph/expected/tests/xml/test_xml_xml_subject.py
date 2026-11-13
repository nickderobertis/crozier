

import pytest

from fern.types.xml_subject import XmlSubject


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlSubject.from_xml("<subject />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlSubject.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlSubject.from_xml('<subject dataUnknown="1"><Unknown a="1">v</Unknown></subject>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlSubject.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlSubject.from_xml("<NotThesubject />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlSubject.from_xml("<subject><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlSubject.from_xml('<!DOCTYPE subject [<!ENTITY xxe "injected">]><subject>&xxe;</subject>')
