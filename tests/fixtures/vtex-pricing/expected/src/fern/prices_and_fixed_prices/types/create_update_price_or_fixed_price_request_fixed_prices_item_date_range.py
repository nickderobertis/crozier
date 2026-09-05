

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class CreateUpdatePriceOrFixedPriceRequestFixedPricesItemDateRange(UniversalBaseModel):
    """
    Period of time when the fixed price will be applied to the SKU.
    """

    from_: typing_extensions.Annotated[
        str, FieldMetadata(alias="from"), pydantic.Field(alias="from", description="Start date of the price.")
    ]
    """
    Start date of the price.
    """

    to: str = pydantic.Field()
    """
    End date of the price.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
