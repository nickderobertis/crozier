

import pytest

from fern.types.create_invalidation_request import CreateInvalidationRequest


def test_from_xml_to_xml_round_trips() -> None:
    parsed = CreateInvalidationRequest.from_xml(
        '<CreateInvalidationRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" />'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert CreateInvalidationRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = CreateInvalidationRequest.from_xml(
        '<CreateInvalidationRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" dataUnknown="1"><Unknown a="1">v</Unknown></CreateInvalidationRequest>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert CreateInvalidationRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        CreateInvalidationRequest.from_xml("<NotTheCreateInvalidationRequest />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        CreateInvalidationRequest.from_xml(
            '<CreateInvalidationRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/"><unclosed>'
        )


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        CreateInvalidationRequest.from_xml(
            '<!DOCTYPE CreateInvalidationRequest [<!ENTITY xxe "injected">]><CreateInvalidationRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/">&xxe;</CreateInvalidationRequest>'
        )
