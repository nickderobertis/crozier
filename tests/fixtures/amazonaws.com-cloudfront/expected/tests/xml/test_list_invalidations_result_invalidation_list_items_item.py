

import pytest

from fern.types.list_invalidations_result_invalidation_list_items_item import (
    ListInvalidationsResultInvalidationListItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = ListInvalidationsResultInvalidationListItemsItem.from_xml("<InvalidationSummary />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        ListInvalidationsResultInvalidationListItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = ListInvalidationsResultInvalidationListItemsItem.from_xml(
        '<InvalidationSummary dataUnknown="1"><Unknown a="1">v</Unknown></InvalidationSummary>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        ListInvalidationsResultInvalidationListItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        ListInvalidationsResultInvalidationListItemsItem.from_xml("<NotTheInvalidationSummary />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        ListInvalidationsResultInvalidationListItemsItem.from_xml("<InvalidationSummary><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        ListInvalidationsResultInvalidationListItemsItem.from_xml(
            '<!DOCTYPE InvalidationSummary [<!ENTITY xxe "injected">]><InvalidationSummary>&xxe;</InvalidationSummary>'
        )
