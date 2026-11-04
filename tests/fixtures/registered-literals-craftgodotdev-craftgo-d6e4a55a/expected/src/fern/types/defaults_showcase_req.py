

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency_code import CurrencyCode
from .order_status import OrderStatus
from .payment_method import PaymentMethod


class DefaultsShowcaseReq(UniversalBaseModel):
    allowed_methods: typing_extensions.Annotated[
        typing.Optional[typing.List[PaymentMethod]],
        FieldMetadata(alias="allowedMethods"),
        pydantic.Field(alias="allowedMethods"),
    ] = None
    currency: typing.Optional[CurrencyCode] = None
    flag: typing.Optional[bool] = None
    num: typing.Optional[int] = None
    preset: typing.Optional[typing.List[str]] = None
    status: typing.Optional[OrderStatus] = None
    str: typing.Optional[str] = None
    tags: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
