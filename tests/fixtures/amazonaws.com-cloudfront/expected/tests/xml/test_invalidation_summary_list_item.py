

import pytest

from fern.types.invalidation_summary_list_item import InvalidationSummaryListItem


def test_from_xml_to_xml_round_trips() -> None:
    parsed = InvalidationSummaryListItem.from_xml("<InvalidationSummary />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert InvalidationSummaryListItem.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = InvalidationSummaryListItem.from_xml(
        '<InvalidationSummary dataUnknown="1"><Unknown a="1">v</Unknown></InvalidationSummary>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert InvalidationSummaryListItem.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        InvalidationSummaryListItem.from_xml("<NotTheInvalidationSummary />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        InvalidationSummaryListItem.from_xml("<InvalidationSummary><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        InvalidationSummaryListItem.from_xml(
            '<!DOCTYPE InvalidationSummary [<!ENTITY xxe "injected">]><InvalidationSummary>&xxe;</InvalidationSummary>'
        )
