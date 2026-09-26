



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .doc_pages_set_scale_request_measure import DocPagesSetScaleRequestMeasure
    from .doc_pages_set_scale_request_measure_angle_item import DocPagesSetScaleRequestMeasureAngleItem
    from .doc_pages_set_scale_request_measure_angle_item_fraction import DocPagesSetScaleRequestMeasureAngleItemFraction
    from .doc_pages_set_scale_request_measure_angle_item_label_position import (
        DocPagesSetScaleRequestMeasureAngleItemLabelPosition,
    )
    from .doc_pages_set_scale_request_measure_area_item import DocPagesSetScaleRequestMeasureAreaItem
    from .doc_pages_set_scale_request_measure_area_item_fraction import DocPagesSetScaleRequestMeasureAreaItemFraction
    from .doc_pages_set_scale_request_measure_area_item_label_position import (
        DocPagesSetScaleRequestMeasureAreaItemLabelPosition,
    )
    from .doc_pages_set_scale_request_measure_distance_item import DocPagesSetScaleRequestMeasureDistanceItem
    from .doc_pages_set_scale_request_measure_distance_item_fraction import (
        DocPagesSetScaleRequestMeasureDistanceItemFraction,
    )
    from .doc_pages_set_scale_request_measure_distance_item_label_position import (
        DocPagesSetScaleRequestMeasureDistanceItemLabelPosition,
    )
    from .doc_pages_set_scale_request_measure_origin import DocPagesSetScaleRequestMeasureOrigin
    from .doc_pages_set_scale_request_measure_slope_item import DocPagesSetScaleRequestMeasureSlopeItem
    from .doc_pages_set_scale_request_measure_slope_item_fraction import DocPagesSetScaleRequestMeasureSlopeItemFraction
    from .doc_pages_set_scale_request_measure_slope_item_label_position import (
        DocPagesSetScaleRequestMeasureSlopeItemLabelPosition,
    )
    from .doc_pages_set_scale_request_measure_subtype import DocPagesSetScaleRequestMeasureSubtype
    from .doc_pages_set_scale_request_measure_x_item import DocPagesSetScaleRequestMeasureXItem
    from .doc_pages_set_scale_request_measure_x_item_fraction import DocPagesSetScaleRequestMeasureXItemFraction
    from .doc_pages_set_scale_request_measure_x_item_label_position import (
        DocPagesSetScaleRequestMeasureXItemLabelPosition,
    )
    from .doc_pages_set_scale_request_measure_y_item import DocPagesSetScaleRequestMeasureYItem
    from .doc_pages_set_scale_request_measure_y_item_fraction import DocPagesSetScaleRequestMeasureYItemFraction
    from .doc_pages_set_scale_request_measure_y_item_label_position import (
        DocPagesSetScaleRequestMeasureYItemLabelPosition,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DocPagesSetScaleRequestMeasure": ".doc_pages_set_scale_request_measure",
    "DocPagesSetScaleRequestMeasureAngleItem": ".doc_pages_set_scale_request_measure_angle_item",
    "DocPagesSetScaleRequestMeasureAngleItemFraction": ".doc_pages_set_scale_request_measure_angle_item_fraction",
    "DocPagesSetScaleRequestMeasureAngleItemLabelPosition": ".doc_pages_set_scale_request_measure_angle_item_label_position",
    "DocPagesSetScaleRequestMeasureAreaItem": ".doc_pages_set_scale_request_measure_area_item",
    "DocPagesSetScaleRequestMeasureAreaItemFraction": ".doc_pages_set_scale_request_measure_area_item_fraction",
    "DocPagesSetScaleRequestMeasureAreaItemLabelPosition": ".doc_pages_set_scale_request_measure_area_item_label_position",
    "DocPagesSetScaleRequestMeasureDistanceItem": ".doc_pages_set_scale_request_measure_distance_item",
    "DocPagesSetScaleRequestMeasureDistanceItemFraction": ".doc_pages_set_scale_request_measure_distance_item_fraction",
    "DocPagesSetScaleRequestMeasureDistanceItemLabelPosition": ".doc_pages_set_scale_request_measure_distance_item_label_position",
    "DocPagesSetScaleRequestMeasureOrigin": ".doc_pages_set_scale_request_measure_origin",
    "DocPagesSetScaleRequestMeasureSlopeItem": ".doc_pages_set_scale_request_measure_slope_item",
    "DocPagesSetScaleRequestMeasureSlopeItemFraction": ".doc_pages_set_scale_request_measure_slope_item_fraction",
    "DocPagesSetScaleRequestMeasureSlopeItemLabelPosition": ".doc_pages_set_scale_request_measure_slope_item_label_position",
    "DocPagesSetScaleRequestMeasureSubtype": ".doc_pages_set_scale_request_measure_subtype",
    "DocPagesSetScaleRequestMeasureXItem": ".doc_pages_set_scale_request_measure_x_item",
    "DocPagesSetScaleRequestMeasureXItemFraction": ".doc_pages_set_scale_request_measure_x_item_fraction",
    "DocPagesSetScaleRequestMeasureXItemLabelPosition": ".doc_pages_set_scale_request_measure_x_item_label_position",
    "DocPagesSetScaleRequestMeasureYItem": ".doc_pages_set_scale_request_measure_y_item",
    "DocPagesSetScaleRequestMeasureYItemFraction": ".doc_pages_set_scale_request_measure_y_item_fraction",
    "DocPagesSetScaleRequestMeasureYItemLabelPosition": ".doc_pages_set_scale_request_measure_y_item_label_position",
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
]
