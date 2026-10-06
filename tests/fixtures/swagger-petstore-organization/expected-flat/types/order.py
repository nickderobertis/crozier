

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .order_status import OrderStatus


class Order(UniversalBaseModel):
    id: typing.Optional[int] = None
    pet_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="petId"), pydantic.Field(alias="petId")
    ] = None
    quantity: typing.Optional[int] = None
    ship_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="shipDate"), pydantic.Field(alias="shipDate")
    ] = None
    status: typing.Optional[OrderStatus] = pydantic.Field(default=None)
    """
    Order Status
    """

    complete: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
