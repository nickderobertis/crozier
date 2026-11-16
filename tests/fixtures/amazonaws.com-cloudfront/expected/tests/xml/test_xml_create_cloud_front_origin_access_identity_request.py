

import pytest

from fern.types.create_cloud_front_origin_access_identity_request import CreateCloudFrontOriginAccessIdentityRequest


def test_from_xml_to_xml_round_trips() -> None:
    parsed = CreateCloudFrontOriginAccessIdentityRequest.from_xml(
        '<CreateCloudFrontOriginAccessIdentityRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" />'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert CreateCloudFrontOriginAccessIdentityRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = CreateCloudFrontOriginAccessIdentityRequest.from_xml(
        '<CreateCloudFrontOriginAccessIdentityRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/" dataUnknown="1"><Unknown a="1">v</Unknown></CreateCloudFrontOriginAccessIdentityRequest>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert CreateCloudFrontOriginAccessIdentityRequest.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        CreateCloudFrontOriginAccessIdentityRequest.from_xml("<NotTheCreateCloudFrontOriginAccessIdentityRequest />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        CreateCloudFrontOriginAccessIdentityRequest.from_xml(
            '<CreateCloudFrontOriginAccessIdentityRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/"><unclosed>'
        )


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        CreateCloudFrontOriginAccessIdentityRequest.from_xml(
            '<!DOCTYPE CreateCloudFrontOriginAccessIdentityRequest [<!ENTITY xxe "injected">]><CreateCloudFrontOriginAccessIdentityRequest xmlns="http://cloudfront.amazonaws.com/doc/2016-11-25/">&xxe;</CreateCloudFrontOriginAccessIdentityRequest>'
        )
