

import pytest

from fern.types.alert_atom_feed import AlertAtomFeed


def test_from_xml_to_xml_round_trips() -> None:
    parsed = AlertAtomFeed.from_xml(
        '<feed xmlns="http://www.w3.org/2005/Atom"><entry xmlns="http://www.w3.org/2005/Atom" /></feed>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert AlertAtomFeed.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = AlertAtomFeed.from_xml(
        '<feed xmlns="http://www.w3.org/2005/Atom" dataUnknown="1"><Unknown a="1">v</Unknown></feed>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert AlertAtomFeed.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        AlertAtomFeed.from_xml("<NotThefeed />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        AlertAtomFeed.from_xml('<feed xmlns="http://www.w3.org/2005/Atom"><unclosed>')


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        AlertAtomFeed.from_xml(
            '<!DOCTYPE feed [<!ENTITY xxe "injected">]><feed xmlns="http://www.w3.org/2005/Atom">&xxe;</feed>'
        )
