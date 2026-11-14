

import pytest

from fern.types.create_distribution_request_distribution_config_cache_behaviors_items_item import (
    CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem.from_xml("<CacheBehavior />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem.from_xml(serialized).to_xml(
            xml_declaration=False
        )
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem.from_xml(
        '<CacheBehavior dataUnknown="1"><Unknown a="1">v</Unknown></CacheBehavior>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem.from_xml(serialized).to_xml(
            xml_declaration=False
        )
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem.from_xml("<NotTheCacheBehavior />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem.from_xml("<CacheBehavior><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        CreateDistributionRequestDistributionConfigCacheBehaviorsItemsItem.from_xml(
            '<!DOCTYPE CacheBehavior [<!ENTITY xxe "injected">]><CacheBehavior>&xxe;</CacheBehavior>'
        )
