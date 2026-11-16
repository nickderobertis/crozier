

import pytest
from PetStore.types.pet import Pet


def test_from_xml_to_xml_round_trips() -> None:
    parsed = Pet.from_xml("<pet><category /><tags><tag /></tags></pet>")
    serialized = parsed.to_xml(xml_declaration=False)
    assert Pet.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = Pet.from_xml('<pet dataUnknown="1"><Unknown a="1">v</Unknown></pet>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert Pet.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        Pet.from_xml("<NotThepet />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        Pet.from_xml("<pet><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        Pet.from_xml('<!DOCTYPE pet [<!ENTITY xxe "injected">]><pet>&xxe;</pet>')
