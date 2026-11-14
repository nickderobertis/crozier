

import pytest

from fern.types.xml_entity import XmlEntity


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlEntity.from_xml('<entity xmlns="http://namespace.openaire.eu/oaf"><project /><result /></entity>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlEntity.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlEntity.from_xml(
        '<entity xmlns="http://namespace.openaire.eu/oaf" dataUnknown="1"><Unknown a="1">v</Unknown></entity>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlEntity.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_preserves_child_order() -> None:
    parsed = XmlEntity.from_xml(
        '<entity xmlns="http://namespace.openaire.eu/oaf"><project /><result /><project /></entity>'
    )
    assert "<project /><result /><project />" in parsed.to_xml(xml_declaration=False)


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlEntity.from_xml("<NotTheentity />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlEntity.from_xml('<entity xmlns="http://namespace.openaire.eu/oaf"><unclosed>')


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlEntity.from_xml(
            '<!DOCTYPE entity [<!ENTITY xxe "injected">]><entity xmlns="http://namespace.openaire.eu/oaf">&xxe;</entity>'
        )
