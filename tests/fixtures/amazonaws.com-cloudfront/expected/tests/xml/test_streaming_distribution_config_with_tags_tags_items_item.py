

import pytest

from fern.types.streaming_distribution_config_with_tags_tags_items_item import (
    StreamingDistributionConfigWithTagsTagsItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = StreamingDistributionConfigWithTagsTagsItemsItem.from_xml("<Tag />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        StreamingDistributionConfigWithTagsTagsItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = StreamingDistributionConfigWithTagsTagsItemsItem.from_xml(
        '<Tag dataUnknown="1"><Unknown a="1">v</Unknown></Tag>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        StreamingDistributionConfigWithTagsTagsItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        StreamingDistributionConfigWithTagsTagsItemsItem.from_xml("<NotTheTag />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        StreamingDistributionConfigWithTagsTagsItemsItem.from_xml("<Tag><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        StreamingDistributionConfigWithTagsTagsItemsItem.from_xml(
            '<!DOCTYPE Tag [<!ENTITY xxe "injected">]><Tag>&xxe;</Tag>'
        )
