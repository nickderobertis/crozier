

import pytest

from fern.types.list_distributions_by_web_acl_id_result_distribution_list_items_item_cache_behaviors_items_item import (
    ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem.from_xml(
        "<CacheBehavior />"
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem.from_xml(serialized).to_xml(
            xml_declaration=False
        )
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem.from_xml(
        '<CacheBehavior dataUnknown="1"><Unknown a="1">v</Unknown></CacheBehavior>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem.from_xml(serialized).to_xml(
            xml_declaration=False
        )
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem.from_xml(
            "<NotTheCacheBehavior />"
        )


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem.from_xml(
            "<CacheBehavior><unclosed>"
        )


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        ListDistributionsByWebAclIdResultDistributionListItemsItemCacheBehaviorsItemsItem.from_xml(
            '<!DOCTYPE CacheBehavior [<!ENTITY xxe "injected">]><CacheBehavior>&xxe;</CacheBehavior>'
        )
