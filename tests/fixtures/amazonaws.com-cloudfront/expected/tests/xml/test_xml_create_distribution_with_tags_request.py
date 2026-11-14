

import pytest

from fern.types.create_distribution_with_tags_request import CreateDistributionWithTagsRequest


def test_from_xml_to_xml_round_trips() -> None:
    parsed = CreateDistributionWithTagsRequest.from_xml(
        '<CreateDistributionWithTagsRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" />'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert CreateDistributionWithTagsRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = CreateDistributionWithTagsRequest.from_xml(
        '<CreateDistributionWithTagsRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" dataUnknown="1"><Unknown a="1">v</Unknown></CreateDistributionWithTagsRequest>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert CreateDistributionWithTagsRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        CreateDistributionWithTagsRequest.from_xml("<NotTheCreateDistributionWithTagsRequest />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        CreateDistributionWithTagsRequest.from_xml(
            '<CreateDistributionWithTagsRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/"><unclosed>'
        )


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        CreateDistributionWithTagsRequest.from_xml(
            '<!DOCTYPE CreateDistributionWithTagsRequest [<!ENTITY xxe "injected">]><CreateDistributionWithTagsRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/">&xxe;</CreateDistributionWithTagsRequest>'
        )
