

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .customer_ref import CustomerRef
from .payment_method import PaymentMethod


class PaymentFailedErr(UniversalBaseModel):
    """
    Conflict error response (HTTP 409).
    """

    charged_by: typing_extensions.Annotated[
        CustomerRef, FieldMetadata(alias="chargedBy"), pydantic.Field(alias="chargedBy")
    ]
    code: typing.Optional[str] = None
    method: PaymentMethod

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
