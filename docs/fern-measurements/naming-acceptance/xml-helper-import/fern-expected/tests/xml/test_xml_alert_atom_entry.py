

import pytest

from fern.types.alert_atom_entry import AlertAtomEntry


def test_from_xml_to_xml_round_trips() -> None:
    parsed = AlertAtomEntry.from_xml('<entry xmlns="http://www.w3.org/2005/Atom" />')
    serialized = parsed.to_xml(xml_declaration=False)
    assert AlertAtomEntry.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = AlertAtomEntry.from_xml(
        '<entry xmlns="http://www.w3.org/2005/Atom" dataUnknown="1"><Unknown a="1">v</Unknown></entry>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert AlertAtomEntry.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        AlertAtomEntry.from_xml("<NotTheentry />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        AlertAtomEntry.from_xml('<entry xmlns="http://www.w3.org/2005/Atom"><unclosed>')


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        AlertAtomEntry.from_xml(
            '<!DOCTYPE entry [<!ENTITY xxe "injected">]><entry xmlns="http://www.w3.org/2005/Atom">&xxe;</entry>'
        )
