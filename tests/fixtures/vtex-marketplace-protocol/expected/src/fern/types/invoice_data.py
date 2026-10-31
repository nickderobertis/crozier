

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_payment_info import UserPaymentInfo


class InvoiceData(UniversalBaseModel):
    """
    Object with the order's billing data.
    """

    user_payment_info: typing_extensions.Annotated[
        UserPaymentInfo, FieldMetadata(alias="userPaymentInfo"), pydantic.Field(alias="userPaymentInfo")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
