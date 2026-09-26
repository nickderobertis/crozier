

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .facets import Facets
from .inventory_facets_response_type import InventoryFacetsResponseType


class InventoryFacetsResponse(UniversalBaseModel):
    """
    Typed AAP response for the `inventory.facets` skill. The `data` object is a Facets aggregation. Carried inside an A2A `Message.parts[].data` DataPart returned from the `SendMessage` operation.
    """

    type: InventoryFacetsResponseType
    data: Facets
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
