

import pytest

from fern.types.probe_result import ProbeResult


def test_from_xml_to_xml_round_trips() -> None:
    parsed = ProbeResult.from_xml("<probe />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert ProbeResult.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = ProbeResult.from_xml('<probe dataUnknown="1"><Unknown a="1">v</Unknown></probe>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert ProbeResult.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        ProbeResult.from_xml("<NotTheprobe />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        ProbeResult.from_xml("<probe><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        ProbeResult.from_xml('<!DOCTYPE probe [<!ENTITY xxe "injected">]><probe>&xxe;</probe>')
