

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .createorupdatefixedpricesonpricetableortradepolicy_request_body_item_date_range import (
    CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItemDateRange,
)


class CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem(UniversalBaseModel):
    date_range: typing_extensions.Annotated[
        typing.Optional[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItemDateRange],
        FieldMetadata(alias="dateRange"),
        pydantic.Field(
            alias="dateRange", description="Period of time when the fixed price will be applied to the SKU."
        ),
    ] = None
    """
    Period of time when the fixed price will be applied to the SKU.
    """

    list_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description="SKU List Fixed Price."),
    ] = None
    """
    SKU List Fixed Price.
    """

    min_quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="minQuantity"),
        pydantic.Field(alias="minQuantity", description="The minimum SKU quantity for the fixed price to be applied."),
    ]
    """
    The minimum SKU quantity for the fixed price to be applied.
    """

    value: float = pydantic.Field()
    """
    Fixed price value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
