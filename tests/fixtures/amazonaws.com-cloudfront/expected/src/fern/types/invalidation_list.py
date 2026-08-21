

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .invalidation_list_items_item import InvalidationListItemsItem


class InvalidationList(UniversalBaseModel):
    """
    The <code>InvalidationList</code> complex type describes the list of invalidation objects. For more information about invalidation, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html">Invalidating Objects (Web Distributions Only)</a> in the <i>Amazon CloudFront Developer Guide</i>.
    """

    marker: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Marker"),
        pydantic.Field(
            alias="Marker", description="The value that you provided for the <code>Marker</code> request parameter."
        ),
    ]
    """
    The value that you provided for the <code>Marker</code> request parameter.
    """

    next_marker: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextMarker"),
        pydantic.Field(
            alias="NextMarker",
            description="If <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value that you can use for the <code>Marker</code> request parameter to continue listing your invalidation batches where they left off.",
        ),
    ] = None
    """
    If <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value that you can use for the <code>Marker</code> request parameter to continue listing your invalidation batches where they left off.
    """

    max_items: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="MaxItems"),
        pydantic.Field(
            alias="MaxItems", description="The value that you provided for the <code>MaxItems</code> request parameter."
        ),
    ]
    """
    The value that you provided for the <code>MaxItems</code> request parameter.
    """

    is_truncated: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="IsTruncated"),
        pydantic.Field(
            alias="IsTruncated",
            description="A flag that indicates whether more invalidation batch requests remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more invalidation batches in the list.",
        ),
    ]
    """
    A flag that indicates whether more invalidation batch requests remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more invalidation batches in the list.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity",
            description="The number of invalidation batches that were created by the current AWS account. ",
        ),
    ]
    """
    The number of invalidation batches that were created by the current AWS account. 
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[InvalidationListItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description="A complex type that contains one <code>InvalidationSummary</code> element for each invalidation batch created by the current AWS account.",
        ),
    ] = None
    """
    A complex type that contains one <code>InvalidationSummary</code> element for each invalidation batch created by the current AWS account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
