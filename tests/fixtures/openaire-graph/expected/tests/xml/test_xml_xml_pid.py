

import pytest

from fern.types.xml_pid import XmlPid


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlPid.from_xml("<pid />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlPid.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlPid.from_xml('<pid dataUnknown="1"><Unknown a="1">v</Unknown></pid>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlPid.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlPid.from_xml("<NotThepid />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlPid.from_xml("<pid><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlPid.from_xml('<!DOCTYPE pid [<!ENTITY xxe "injected">]><pid>&xxe;</pid>')
