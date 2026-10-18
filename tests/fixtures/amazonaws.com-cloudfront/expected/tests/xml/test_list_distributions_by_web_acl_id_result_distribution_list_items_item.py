

import pytest

from fern.types.list_distributions_by_web_acl_id_result_distribution_list_items_item import (
    ListDistributionsByWebAclIdResultDistributionListItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = ListDistributionsByWebAclIdResultDistributionListItemsItem.from_xml("<DistributionSummary />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        ListDistributionsByWebAclIdResultDistributionListItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = ListDistributionsByWebAclIdResultDistributionListItemsItem.from_xml(
        '<DistributionSummary dataUnknown="1"><Unknown a="1">v</Unknown></DistributionSummary>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        ListDistributionsByWebAclIdResultDistributionListItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        ListDistributionsByWebAclIdResultDistributionListItemsItem.from_xml("<NotTheDistributionSummary />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        ListDistributionsByWebAclIdResultDistributionListItemsItem.from_xml("<DistributionSummary><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        ListDistributionsByWebAclIdResultDistributionListItemsItem.from_xml(
            '<!DOCTYPE DistributionSummary [<!ENTITY xxe "injected">]><DistributionSummary>&xxe;</DistributionSummary>'
        )
