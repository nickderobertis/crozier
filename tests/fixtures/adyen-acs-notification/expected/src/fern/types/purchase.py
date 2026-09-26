

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount


class Purchase(UniversalBaseModel):
    date: dt.datetime = pydantic.Field()
    """
    The time of the purchase.
    """

    merchant_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="merchantName"),
        pydantic.Field(alias="merchantName", description="The name of the merchant."),
    ]
    """
    The name of the merchant.
    """

    original_amount: typing_extensions.Annotated[
        Amount,
        FieldMetadata(alias="originalAmount"),
        pydantic.Field(alias="originalAmount", description="The amount of the purchase in the original currency."),
    ]
    """
    The amount of the purchase in the original currency.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
