



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_phases_job_phase_id_stock_on_hand_request_sort_field import GetPhasesJobPhaseIdStockOnHandRequestSortField
    from .get_phases_job_phase_id_stock_on_hand_request_sort_order import GetPhasesJobPhaseIdStockOnHandRequestSortOrder
    from .get_phases_stock_on_hand_request_sort_field import GetPhasesStockOnHandRequestSortField
    from .get_phases_stock_on_hand_request_sort_order import GetPhasesStockOnHandRequestSortOrder
    from .post_phases_job_phase_id_stock_on_hand_request_body import PostPhasesJobPhaseIdStockOnHandRequestBody
    from .post_phases_job_phase_id_stock_on_hand_request_body_item_cost import (
        PostPhasesJobPhaseIdStockOnHandRequestBodyItemCost,
    )
    from .post_phases_job_phase_id_stock_on_hand_request_body_price_book_line_item_id import (
        PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetPhasesJobPhaseIdStockOnHandRequestSortField": ".get_phases_job_phase_id_stock_on_hand_request_sort_field",
    "GetPhasesJobPhaseIdStockOnHandRequestSortOrder": ".get_phases_job_phase_id_stock_on_hand_request_sort_order",
    "GetPhasesStockOnHandRequestSortField": ".get_phases_stock_on_hand_request_sort_field",
    "GetPhasesStockOnHandRequestSortOrder": ".get_phases_stock_on_hand_request_sort_order",
    "PostPhasesJobPhaseIdStockOnHandRequestBody": ".post_phases_job_phase_id_stock_on_hand_request_body",
    "PostPhasesJobPhaseIdStockOnHandRequestBodyItemCost": ".post_phases_job_phase_id_stock_on_hand_request_body_item_cost",
    "PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId": ".post_phases_job_phase_id_stock_on_hand_request_body_price_book_line_item_id",
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
    "GetPhasesJobPhaseIdStockOnHandRequestSortField",
    "GetPhasesJobPhaseIdStockOnHandRequestSortOrder",
    "GetPhasesStockOnHandRequestSortField",
    "GetPhasesStockOnHandRequestSortOrder",
    "PostPhasesJobPhaseIdStockOnHandRequestBody",
    "PostPhasesJobPhaseIdStockOnHandRequestBodyItemCost",
    "PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId",
]
