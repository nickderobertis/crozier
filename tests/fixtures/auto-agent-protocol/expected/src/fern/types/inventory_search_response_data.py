

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .facets import Facets
from .inventory_search_response_data_vehicles_item import InventorySearchResponseDataVehiclesItem


class InventorySearchResponseData(UniversalBaseModel):
    total: int = pydantic.Field()
    """
    Total number of vehicles matching the request (across all pages).
    """

    skip: typing.Optional[int] = pydantic.Field(default=None)
    """
    Echo of the request's pagination.skip.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Echo of the request's effective pagination.limit.
    """

    vehicles: typing.List[InventorySearchResponseDataVehiclesItem] = pydantic.Field()
    """
    Vehicles in this page, in the requested order. Each item is a Vehicle constrained to the sale-condition vocabulary (`new`|`used`|`cpo`) — inventory listings never carry trade-in wear values — and MUST carry a `status` of `available`, `intransit`, or `pending`. Out-of-stock vehicles are never returned.
    """

    facets: typing.Optional[Facets] = pydantic.Field(default=None)
    """
    Optional aggregated facets over the matching set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
