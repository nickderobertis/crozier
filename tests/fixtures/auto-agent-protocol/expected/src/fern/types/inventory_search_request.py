

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inventory_search_request_pagination import InventorySearchRequestPagination
from .inventory_search_request_privacy import InventorySearchRequestPrivacy
from .inventory_search_request_sort import InventorySearchRequestSort
from .inventory_search_request_type import InventorySearchRequestType


class InventorySearchRequest(UniversalBaseModel):
    """
    Typed AAP request for the `inventory.search` skill. Filters are FLAT (no nested make/model trees) and multi-value filters are arrays. Pagination uses skip/limit; sort is field+order. `privacy.anonymous` declares whether the buyer agent is sharing user identity. Carried inside an A2A `Message.parts[].data` DataPart via the A2A `SendMessage` operation.
    """

    type: InventorySearchRequestType
    filters: typing.Optional[typing.Any] = None
    pagination: typing.Optional[InventorySearchRequestPagination] = pydantic.Field(default=None)
    """
    Result paging. Default values are dealer-defined; spec recommends limit defaults <= 50 and limit cap of 100.
    """

    sort: typing.Optional[InventorySearchRequestSort] = pydantic.Field(default=None)
    """
    Result ordering. Default ordering is dealer-defined.
    """

    privacy: typing.Optional[InventorySearchRequestPrivacy] = pydantic.Field(default=None)
    """
    Privacy hints from the buyer agent. AAP RECOMMENDS anonymous searches by default; user identity is only attached when a lead is submitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
