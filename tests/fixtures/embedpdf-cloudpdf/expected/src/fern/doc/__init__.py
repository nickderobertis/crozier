



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from . import annotations, forms, metadata, pages, redactions, signatures, versions
    from .forms import ExportDataFormsRequestFormat
    from .pages import (
        DocPagesSetScaleRequestMeasure,
        DocPagesSetScaleRequestMeasureAngleItem,
        DocPagesSetScaleRequestMeasureAngleItemFraction,
        DocPagesSetScaleRequestMeasureAngleItemLabelPosition,
        DocPagesSetScaleRequestMeasureAreaItem,
        DocPagesSetScaleRequestMeasureAreaItemFraction,
        DocPagesSetScaleRequestMeasureAreaItemLabelPosition,
        DocPagesSetScaleRequestMeasureDistanceItem,
        DocPagesSetScaleRequestMeasureDistanceItemFraction,
        DocPagesSetScaleRequestMeasureDistanceItemLabelPosition,
        DocPagesSetScaleRequestMeasureOrigin,
        DocPagesSetScaleRequestMeasureSlopeItem,
        DocPagesSetScaleRequestMeasureSlopeItemFraction,
        DocPagesSetScaleRequestMeasureSlopeItemLabelPosition,
        DocPagesSetScaleRequestMeasureSubtype,
        DocPagesSetScaleRequestMeasureXItem,
        DocPagesSetScaleRequestMeasureXItemFraction,
        DocPagesSetScaleRequestMeasureXItemLabelPosition,
        DocPagesSetScaleRequestMeasureYItem,
        DocPagesSetScaleRequestMeasureYItemFraction,
        DocPagesSetScaleRequestMeasureYItemLabelPosition,
    )
    from .signatures import AnalysisSignaturesRequestLevel, DocSignaturesCompleteRequestExpectedVersion
    from .versions import AnalysisVersionsRequestLevel, SignatureDigestVersionsRequestAlgorithm
_dynamic_imports: typing.Dict[str, str] = {
    "AnalysisSignaturesRequestLevel": ".signatures",
    "AnalysisVersionsRequestLevel": ".versions",
    "DocPagesSetScaleRequestMeasure": ".pages",
    "DocPagesSetScaleRequestMeasureAngleItem": ".pages",
    "DocPagesSetScaleRequestMeasureAngleItemFraction": ".pages",
    "DocPagesSetScaleRequestMeasureAngleItemLabelPosition": ".pages",
    "DocPagesSetScaleRequestMeasureAreaItem": ".pages",
    "DocPagesSetScaleRequestMeasureAreaItemFraction": ".pages",
    "DocPagesSetScaleRequestMeasureAreaItemLabelPosition": ".pages",
    "DocPagesSetScaleRequestMeasureDistanceItem": ".pages",
    "DocPagesSetScaleRequestMeasureDistanceItemFraction": ".pages",
    "DocPagesSetScaleRequestMeasureDistanceItemLabelPosition": ".pages",
    "DocPagesSetScaleRequestMeasureOrigin": ".pages",
    "DocPagesSetScaleRequestMeasureSlopeItem": ".pages",
    "DocPagesSetScaleRequestMeasureSlopeItemFraction": ".pages",
    "DocPagesSetScaleRequestMeasureSlopeItemLabelPosition": ".pages",
    "DocPagesSetScaleRequestMeasureSubtype": ".pages",
    "DocPagesSetScaleRequestMeasureXItem": ".pages",
    "DocPagesSetScaleRequestMeasureXItemFraction": ".pages",
    "DocPagesSetScaleRequestMeasureXItemLabelPosition": ".pages",
    "DocPagesSetScaleRequestMeasureYItem": ".pages",
    "DocPagesSetScaleRequestMeasureYItemFraction": ".pages",
    "DocPagesSetScaleRequestMeasureYItemLabelPosition": ".pages",
    "DocSignaturesCompleteRequestExpectedVersion": ".signatures",
    "ExportDataFormsRequestFormat": ".forms",
    "SignatureDigestVersionsRequestAlgorithm": ".versions",
    "annotations": ".annotations",
    "forms": ".forms",
    "metadata": ".metadata",
    "pages": ".pages",
    "redactions": ".redactions",
    "signatures": ".signatures",
    "versions": ".versions",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AnalysisSignaturesRequestLevel",
    "AnalysisVersionsRequestLevel",
    "DocPagesSetScaleRequestMeasure",
    "DocPagesSetScaleRequestMeasureAngleItem",
    "DocPagesSetScaleRequestMeasureAngleItemFraction",
    "DocPagesSetScaleRequestMeasureAngleItemLabelPosition",
    "DocPagesSetScaleRequestMeasureAreaItem",
    "DocPagesSetScaleRequestMeasureAreaItemFraction",
    "DocPagesSetScaleRequestMeasureAreaItemLabelPosition",
    "DocPagesSetScaleRequestMeasureDistanceItem",
    "DocPagesSetScaleRequestMeasureDistanceItemFraction",
    "DocPagesSetScaleRequestMeasureDistanceItemLabelPosition",
    "DocPagesSetScaleRequestMeasureOrigin",
    "DocPagesSetScaleRequestMeasureSlopeItem",
    "DocPagesSetScaleRequestMeasureSlopeItemFraction",
    "DocPagesSetScaleRequestMeasureSlopeItemLabelPosition",
    "DocPagesSetScaleRequestMeasureSubtype",
    "DocPagesSetScaleRequestMeasureXItem",
    "DocPagesSetScaleRequestMeasureXItemFraction",
    "DocPagesSetScaleRequestMeasureXItemLabelPosition",
    "DocPagesSetScaleRequestMeasureYItem",
    "DocPagesSetScaleRequestMeasureYItemFraction",
    "DocPagesSetScaleRequestMeasureYItemLabelPosition",
    "DocSignaturesCompleteRequestExpectedVersion",
    "ExportDataFormsRequestFormat",
    "SignatureDigestVersionsRequestAlgorithm",
    "annotations",
    "forms",
    "metadata",
    "pages",
    "redactions",
    "signatures",
    "versions",
]
