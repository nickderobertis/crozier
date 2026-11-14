

import pytest

from fern.types.streaming_distribution_summary_list_item import StreamingDistributionSummaryListItem


def test_from_xml_to_xml_round_trips() -> None:
    parsed = StreamingDistributionSummaryListItem.from_xml("<StreamingDistributionSummary />")
    serialized = parsed.to_xml(xml_declaration=False)
    assert StreamingDistributionSummaryListItem.from_xml(serialized).to_xml(xml_declaration=False) == serialized
    assert parsed.to_xml().startswith('<?xml version="1.0"')
    assert str(parsed) == parsed.to_xml()


def test_from_xml_preserves_unknown_attributes_and_children() -> None:
    parsed = StreamingDistributionSummaryListItem.from_xml(
        '<StreamingDistributionSummary dataUnknown="1"><Unknown a="1">v</Unknown></StreamingDistributionSummary>'
    )
    serialized = parsed.to_xml(xml_declaration=False)
    assert 'dataUnknown="1"' in serialized
    assert '<Unknown a="1">v</Unknown>' in serialized
    assert StreamingDistributionSummaryListItem.from_xml(serialized).to_xml(xml_declaration=False) == serialized


def test_from_xml_rejects_wrong_root_element() -> None:
    with pytest.raises(ValueError):
        StreamingDistributionSummaryListItem.from_xml("<NotTheStreamingDistributionSummary />")


def test_from_xml_rejects_malformed_xml() -> None:
    with pytest.raises(ValueError):
        StreamingDistributionSummaryListItem.from_xml("<StreamingDistributionSummary><unclosed>")


def test_from_xml_rejects_doctype() -> None:
    with pytest.raises(ValueError):
        StreamingDistributionSummaryListItem.from_xml(
            '<!DOCTYPE StreamingDistributionSummary [<!ENTITY xxe "injected">]><StreamingDistributionSummary>&xxe;</StreamingDistributionSummary>'
        )
