

import pytest

from fern.types.xml_contract_type import XmlContractType


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlContractType.from_xml("<contracttype />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlContractType.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlContractType.from_xml('<contracttype dataUnknown="1"><Unknown a="1">v</Unknown></contracttype>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlContractType.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlContractType.from_xml("<NotThecontracttype />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlContractType.from_xml("<contracttype><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlContractType.from_xml('<!DOCTYPE contracttype [<!ENTITY xxe "injected">]><contracttype>&xxe;</contracttype>')
