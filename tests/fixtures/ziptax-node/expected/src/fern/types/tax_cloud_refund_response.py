

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_refund_item_response import TaxCloudRefundItemResponse


class TaxCloudRefundResponse(UniversalBaseModel):
    batch_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="batchId"),
        pydantic.Field(
            alias="batchId", description="Batch ID grouping this refund with related refunds, if one was supplied."
        ),
    ] = None
    """
    Batch ID grouping this refund with related refunds, if one was supplied.
    """

    connection_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connectionId"),
        pydantic.Field(alias="connectionId", description="The TaxCloud connection the refund was recorded under."),
    ]
    """
    The TaxCloud connection the refund was recorded under.
    """

    created_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdDate"),
        pydantic.Field(alias="createdDate", description="RFC3339 datetime the refund was created."),
    ] = None
    """
    RFC3339 datetime the refund was created.
    """

    items: typing.Optional[typing.List[TaxCloudRefundItemResponse]] = pydantic.Field(default=None)
    """
    The refunded line items, each with the refunded price, quantity, and tax amount.
    """

    returned_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="returnedDate"),
        pydantic.Field(alias="returnedDate", description="RFC3339 datetime the refund took effect."),
    ] = None
    """
    RFC3339 datetime the refund took effect.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
