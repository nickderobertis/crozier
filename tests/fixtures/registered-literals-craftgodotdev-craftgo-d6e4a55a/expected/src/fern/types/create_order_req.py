

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency_code import CurrencyCode
from .line_item import LineItem
from .non_empty_id import NonEmptyId


class CreateOrderReq(UniversalBaseModel):
    currency: typing.Optional[CurrencyCode] = None
    customer_id: typing_extensions.Annotated[
        NonEmptyId, FieldMetadata(alias="customerId"), pydantic.Field(alias="customerId")
    ]
    items: typing.List[LineItem]
    notes: typing.Optional[str] = None
    tags: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
