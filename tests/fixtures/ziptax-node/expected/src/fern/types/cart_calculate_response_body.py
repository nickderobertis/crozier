

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_cart_response import TaxCloudCartResponse


class CartCalculateResponseBody(UniversalBaseModel):
    connection_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connectionId"),
        pydantic.Field(alias="connectionId", description="The TaxCloud connection the calculation ran under."),
    ]
    """
    The TaxCloud connection the calculation ran under.
    """

    items: typing.Optional[typing.List[TaxCloudCartResponse]] = pydantic.Field(default=None)
    """
    One calculated cart per submitted cart, in the same order, with per-line-item tax rates and amounts.
    """

    transaction_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="transactionDate"),
        pydantic.Field(alias="transactionDate", description="RFC3339 datetime the carts were calculated for."),
    ] = None
    """
    RFC3339 datetime the carts were calculated for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
