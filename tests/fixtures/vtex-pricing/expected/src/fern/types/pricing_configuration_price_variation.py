

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PricingConfigurationPriceVariation(UniversalBaseModel):
    """
    Price Variation object.
    """

    lower_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lowerLimit"),
        pydantic.Field(alias="lowerLimit", description="Lower variation limit."),
    ] = None
    """
    Lower variation limit.
    """

    upper_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="upperLimit"),
        pydantic.Field(alias="upperLimit", description="Upper variation limit."),
    ] = None
    """
    Upper variation limit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
