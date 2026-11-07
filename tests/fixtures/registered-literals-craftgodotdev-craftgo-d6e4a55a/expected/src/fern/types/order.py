

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency_code import CurrencyCode
from .customer import Customer
from .customer_ref import CustomerRef
from .line_item import LineItem
from .non_empty_id import NonEmptyId
from .order_status import OrderStatus
from .payment import Payment


class Order(UniversalBaseModel):
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    created_by: typing_extensions.Annotated[
        CustomerRef, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ]
    currency: typing.Optional[CurrencyCode] = None
    customer: Customer
    extras: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Free-form provider payload, e.g. { trackingNumber, carrier }.
    """

    grid: typing.List[typing.List[str]]
    id: NonEmptyId
    items: typing.List[LineItem]
    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    notes: typing.Optional[str] = None
    payment: typing.Optional[Payment] = None
    shipped_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="shippedAt"), pydantic.Field(alias="shippedAt")
    ] = None
    status: OrderStatus
    tags: typing.List[str]
    total_cents: typing_extensions.Annotated[int, FieldMetadata(alias="totalCents"), pydantic.Field(alias="totalCents")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
