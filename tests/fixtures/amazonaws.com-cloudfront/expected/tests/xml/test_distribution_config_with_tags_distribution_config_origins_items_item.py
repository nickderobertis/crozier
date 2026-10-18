

import pytest

from fern.types.distribution_config_with_tags_distribution_config_origins_items_item import (
    DistributionConfigWithTagsDistributionConfigOriginsItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = DistributionConfigWithTagsDistributionConfigOriginsItemsItem.from_xml("<Origin />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = DistributionConfigWithTagsDistributionConfigOriginsItemsItem.from_xml(
        '<Origin dataUnknown="1"><Unknown a="1">v</Unknown></Origin>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        DistributionConfigWithTagsDistributionConfigOriginsItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        DistributionConfigWithTagsDistributionConfigOriginsItemsItem.from_xml("<NotTheOrigin />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        DistributionConfigWithTagsDistributionConfigOriginsItemsItem.from_xml("<Origin><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        DistributionConfigWithTagsDistributionConfigOriginsItemsItem.from_xml(
            '<!DOCTYPE Origin [<!ENTITY xxe "injected">]><Origin>&xxe;</Origin>'
        )
