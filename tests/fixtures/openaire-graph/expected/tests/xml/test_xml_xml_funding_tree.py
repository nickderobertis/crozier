

import pytest

from fern.types.xml_funding_tree import XmlFundingTree


def test_from_xml_to_xml_round_trips() -> None:
    parsed = XmlFundingTree.from_xml("<fundingtree><funder /></fundingtree>")
    serialized = parsed.to_xml(xml_declaration=False)
    assert XmlFundingTree.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = XmlFundingTree.from_xml('<fundingtree dataUnknown="1"><Unknown a="1">v</Unknown></fundingtree>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert XmlFundingTree.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        XmlFundingTree.from_xml("<NotThefundingtree />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        XmlFundingTree.from_xml("<fundingtree><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        XmlFundingTree.from_xml('<!DOCTYPE fundingtree [<!ENTITY xxe "injected">]><fundingtree>&xxe;</fundingtree>')
