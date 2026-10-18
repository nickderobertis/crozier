

import pytest

from fern.types.update_streaming_distribution_request import UpdateStreamingDistributionRequest


def test_from_xml_to_xml_round_trips() -> None:
    parsed = UpdateStreamingDistributionRequest.from_xml(
        '<UpdateStreamingDistributionRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" />'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert UpdateStreamingDistributionRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = UpdateStreamingDistributionRequest.from_xml(
        '<UpdateStreamingDistributionRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" dataUnknown="1"><Unknown a="1">v</Unknown></UpdateStreamingDistributionRequest>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert UpdateStreamingDistributionRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        UpdateStreamingDistributionRequest.from_xml("<NotTheUpdateStreamingDistributionRequest />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        UpdateStreamingDistributionRequest.from_xml(
            '<UpdateStreamingDistributionRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/"><unclosed>'
        )


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        UpdateStreamingDistributionRequest.from_xml(
            '<!DOCTYPE UpdateStreamingDistributionRequest [<!ENTITY xxe "injected">]><UpdateStreamingDistributionRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/">&xxe;</UpdateStreamingDistributionRequest>'
        )
