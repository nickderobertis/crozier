

import pytest

from fern.types.tag_resource_request import TagResourceRequest


def test_from_xml_to_xml_round_trips() -> None:
    parsed = TagResourceRequest.from_xml(
        '<TagResourceRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" />'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert TagResourceRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = TagResourceRequest.from_xml(
        '<TagResourceRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" dataUnknown="1"><Unknown a="1">v</Unknown></TagResourceRequest>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert TagResourceRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        TagResourceRequest.from_xml("<NotTheTagResourceRequest />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        TagResourceRequest.from_xml(
            '<TagResourceRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/"><unclosed>'
        )


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        TagResourceRequest.from_xml(
            '<!DOCTYPE TagResourceRequest [<!ENTITY xxe "injected">]><TagResourceRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/">&xxe;</TagResourceRequest>'
        )
