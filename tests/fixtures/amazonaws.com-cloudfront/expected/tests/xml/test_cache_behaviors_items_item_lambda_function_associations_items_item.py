

import pytest

from fern.types.cache_behaviors_items_item_lambda_function_associations_items_item import (
    CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
)


def test_from_xml_to_xml_round_trips() -> None:
    parsed = CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem.from_xml("<LambdaFunctionAssociation />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert (
        CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem.from_xml(
        '<LambdaFunctionAssociation dataUnknown="1"><Unknown a="1">v</Unknown></LambdaFunctionAssociation>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert (
        CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem.from_xml(serialized).to_xml(xml_declaration=False)
        == serialized
    )


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem.from_xml("<NotTheLambdaFunctionAssociation />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem.from_xml("<LambdaFunctionAssociation><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem.from_xml(
            '<!DOCTYPE LambdaFunctionAssociation [<!ENTITY xxe "injected">]><LambdaFunctionAssociation>&xxe;</LambdaFunctionAssociation>'
        )
