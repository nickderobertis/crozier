

import pytest

from fern.types.distribution_active_trusted_signers_items_item import DistributionActiveTrustedSignersItemsItem


def test_from_xml_to_xml_round_trips() -> None:
    parsed = DistributionActiveTrustedSignersItemsItem.from_xml("<Signer />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert DistributionActiveTrustedSignersItemsItem.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = DistributionActiveTrustedSignersItemsItem.from_xml(
        '<Signer dataUnknown="1"><Unknown a="1">v</Unknown></Signer>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert DistributionActiveTrustedSignersItemsItem.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        DistributionActiveTrustedSignersItemsItem.from_xml("<NotTheSigner />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        DistributionActiveTrustedSignersItemsItem.from_xml("<Signer><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        DistributionActiveTrustedSignersItemsItem.from_xml(
            '<!DOCTYPE Signer [<!ENTITY xxe "injected">]><Signer>&xxe;</Signer>'
        )
