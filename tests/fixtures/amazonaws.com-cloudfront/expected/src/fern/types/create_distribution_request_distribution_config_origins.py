

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_distribution_request_distribution_config_origins_items_item import (
    CreateDistributionRequestDistributionConfigOriginsItemsItem,
)


class CreateDistributionRequestDistributionConfigOrigins(UniversalBaseModel):
    """
    A complex type that contains information about origins for this distribution.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(alias="Quantity", description="The number of origins for this distribution."),
    ]
    """
    The number of origins for this distribution.
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[CreateDistributionRequestDistributionConfigOriginsItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(alias="Items", description="A complex type that contains origins for this distribution."),
    ] = None
    """
    A complex type that contains origins for this distribution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
