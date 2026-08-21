

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .distribution_list_items_item import DistributionListItemsItem


class DistributionList(UniversalBaseModel):
    """
    A distribution list.
    """

    marker: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Marker"),
        pydantic.Field(
            alias="Marker", description="The value you provided for the <code>Marker</code> request parameter."
        ),
    ]
    """
    The value you provided for the <code>Marker</code> request parameter.
    """

    next_marker: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextMarker"),
        pydantic.Field(
            alias="NextMarker",
            description="If <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value you can use for the <code>Marker</code> request parameter to continue listing your distributions where they left off. ",
        ),
    ] = None
    """
    If <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value you can use for the <code>Marker</code> request parameter to continue listing your distributions where they left off. 
    """

    max_items: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="MaxItems"),
        pydantic.Field(
            alias="MaxItems", description="The value you provided for the <code>MaxItems</code> request parameter."
        ),
    ]
    """
    The value you provided for the <code>MaxItems</code> request parameter.
    """

    is_truncated: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="IsTruncated"),
        pydantic.Field(
            alias="IsTruncated",
            description="A flag that indicates whether more distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more distributions in the list.",
        ),
    ]
    """
    A flag that indicates whether more distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more distributions in the list.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity", description="The number of distributions that were created by the current AWS account. "
        ),
    ]
    """
    The number of distributions that were created by the current AWS account. 
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[DistributionListItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description="A complex type that contains one <code>DistributionSummary</code> element for each distribution that was created by the current AWS account.",
        ),
    ] = None
    """
    A complex type that contains one <code>DistributionSummary</code> element for each distribution that was created by the current AWS account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
