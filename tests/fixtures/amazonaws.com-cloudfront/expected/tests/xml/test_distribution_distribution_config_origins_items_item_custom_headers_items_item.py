

import pytest

from fern.types.distribution_distribution_config_origins_items_item_custom_headers_items_item import (
    DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem.from_xml("<OriginCustomHeader />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem.from_xml(serialized).to_xml(
            xml_declaration=False
        )
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem.from_xml(
        '<OriginCustomHeader dataUnknown="1"><Unknown a="1">v</Unknown></OriginCustomHeader>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem.from_xml(serialized).to_xml(
            xml_declaration=False
        )
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem.from_xml("<NotTheOriginCustomHeader />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem.from_xml("<OriginCustomHeader><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        DistributionDistributionConfigOriginsItemsItemCustomHeadersItemsItem.from_xml(
            '<!DOCTYPE OriginCustomHeader [<!ENTITY xxe "injected">]><OriginCustomHeader>&xxe;</OriginCustomHeader>'
        )
