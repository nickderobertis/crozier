

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inventory_search_request_sort_field import InventorySearchRequestSortField
from .inventory_search_request_sort_order import InventorySearchRequestSortOrder


class InventorySearchRequestSort(UniversalBaseModel):
    """
    Result ordering. Default ordering is dealer-defined.
    """

    field: InventorySearchRequestSortField = pydantic.Field()
    """
    Field to sort by. Sorting by 'price' uses the FTC-final 'price' field (which dealers MUST keep accurate); 'updated_at' sorts by listing freshness.
    """

    order: InventorySearchRequestSortOrder

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
