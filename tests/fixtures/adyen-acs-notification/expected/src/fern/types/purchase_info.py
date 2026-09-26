

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount


class PurchaseInfo(UniversalBaseModel):
    date: str = pydantic.Field()
    """
    The date of the purchase.
    """

    merchant_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="merchantName"),
        pydantic.Field(
            alias="merchantName", description="The name of the business that the cardholder purchased from."
        ),
    ]
    """
    The name of the business that the cardholder purchased from.
    """

    original_amount: typing_extensions.Annotated[
        Amount,
        FieldMetadata(alias="originalAmount"),
        pydantic.Field(alias="originalAmount", description="The amount of the purchase."),
    ]
    """
    The amount of the purchase.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
