

import pytest

from fern.types.api_response import ApiResponse


def test_from_xml_to_xml_round_trips() -> None:
    parsed = ApiResponse.from_xml("<##default />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert ApiResponse.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = ApiResponse.from_xml('<##default dataUnknown="1"><Unknown a="1">v</Unknown></##default>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert ApiResponse.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        ApiResponse.from_xml("<NotThe##default />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        ApiResponse.from_xml("<##default><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        ApiResponse.from_xml('<!DOCTYPE ##default [<!ENTITY xxe "injected">]><##default>&xxe;</##default>')
