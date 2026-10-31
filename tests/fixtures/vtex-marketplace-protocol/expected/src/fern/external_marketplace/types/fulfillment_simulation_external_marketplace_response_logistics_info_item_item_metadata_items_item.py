

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadataItemsItem(UniversalBaseModel):
    assembly_options: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="assemblyOptions"),
        pydantic.Field(alias="assemblyOptions", description="Assembly options information."),
    ] = None
    """
    Assembly options information.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Item ID.
    """

    seller: typing.Optional[str] = pydantic.Field(default=None)
    """
    Seller.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
