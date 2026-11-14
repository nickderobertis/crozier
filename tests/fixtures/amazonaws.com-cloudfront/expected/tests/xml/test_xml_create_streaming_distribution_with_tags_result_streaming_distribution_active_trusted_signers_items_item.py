

import pytest

from fern.types.create_streaming_distribution_with_tags_result_streaming_distribution_active_trusted_signers_items_item import (
    CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem.from_xml(
        "<Signer />"
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem.from_xml(
            serialized
        ).to_xml(xml_declaration=False)
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem.from_xml(
        '<Signer dataUnknown="1"><Unknown a="1">v</Unknown></Signer>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem.from_xml(
            serialized
        ).to_xml(xml_declaration=False)
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem.from_xml(
            "<NotTheSigner />"
        )


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem.from_xml(
            "<Signer><unclosed>"
        )


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        CreateStreamingDistributionWithTagsResultStreamingDistributionActiveTrustedSignersItemsItem.from_xml(
            '<!DOCTYPE Signer [<!ENTITY xxe "injected">]><Signer>&xxe;</Signer>'
        )
