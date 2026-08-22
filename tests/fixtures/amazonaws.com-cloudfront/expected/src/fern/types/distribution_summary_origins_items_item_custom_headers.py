

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .distribution_summary_origins_items_item_custom_headers_items_item import (
    DistributionSummaryOriginsItemsItemCustomHeadersItemsItem,
)


class DistributionSummaryOriginsItemsItemCustomHeaders(UniversalBaseModel):
    """
    A complex type that contains names and values for the custom headers that you want.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(alias="Quantity", description="The number of custom headers, if any, for this distribution."),
    ]
    """
    The number of custom headers, if any, for this distribution.
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[DistributionSummaryOriginsItemsItemCustomHeadersItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description=" <b>Optional</b>: A list that contains one <code>OriginCustomHeader</code> element for each custom header that you want CloudFront to forward to the origin. If Quantity is <code>0</code>, omit <code>Items</code>.",
        ),
    ] = None
    """
     <b>Optional</b>: A list that contains one <code>OriginCustomHeader</code> element for each custom header that you want CloudFront to forward to the origin. If Quantity is <code>0</code>, omit <code>Items</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
