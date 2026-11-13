

import pytest

from fern.types.similar_company_search import SimilarCompanySearch


def test_from_xml_to_xml_round_trips() -> None:
    parsed = SimilarCompanySearch.from_xml("<Order />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert SimilarCompanySearch.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = SimilarCompanySearch.from_xml('<Order dataUnknown="1"><Unknown a="1">v</Unknown></Order>')
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert SimilarCompanySearch.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        SimilarCompanySearch.from_xml("<NotTheOrder />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        SimilarCompanySearch.from_xml("<Order><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        SimilarCompanySearch.from_xml('<!DOCTYPE Order [<!ENTITY xxe "injected">]><Order>&xxe;</Order>')
