

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inventory_facets_request_type import InventoryFacetsRequestType


class InventoryFacetsRequest(UniversalBaseModel):
    """
    Typed AAP request for the `inventory.facets` skill. An optional `filters` block scopes the facets to a subset of inventory (e.g. `condition: ['used']`). Carried inside an A2A `Message.parts[].data` DataPart via the A2A `SendMessage` operation.
    """

    type: InventoryFacetsRequestType
    filters: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
