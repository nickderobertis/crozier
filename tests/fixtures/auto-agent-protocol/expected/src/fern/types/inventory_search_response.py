

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inventory_search_response_data import InventorySearchResponseData
from .inventory_search_response_type import InventorySearchResponseType


class InventorySearchResponse(UniversalBaseModel):
    """
    Typed AAP response for the `inventory.search` skill. The `data` block contains pagination metadata, the matched vehicles, and OPTIONALLY an embedded Facets aggregation. Carried inside an A2A `Message.parts[].data` DataPart returned from the `SendMessage` operation.
    """

    type: InventorySearchResponseType
    data: InventorySearchResponseData
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional contextual note. MAY be omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
