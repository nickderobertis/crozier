

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cloud_front_origin_access_identity_list_items_item import CloudFrontOriginAccessIdentityListItemsItem


class CloudFrontOriginAccessIdentityList(UniversalBaseModel):
    """
    Lists the origin access identities for CloudFront.Send a <code>GET</code> request to the <code>/<i>CloudFront API version</i>/origin-access-identity/cloudfront</code> resource. The response includes a <code>CloudFrontOriginAccessIdentityList</code> element with zero or more <code>CloudFrontOriginAccessIdentitySummary</code> child elements. By default, your entire list of origin access identities is returned in one single page. If the list is long, you can paginate it using the <code>MaxItems</code> and <code>Marker</code> parameters.
    """

    marker: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Marker"),
        pydantic.Field(
            alias="Marker",
            description="Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page). ",
        ),
    ]
    """
    Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page). 
    """

    next_marker: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextMarker"),
        pydantic.Field(
            alias="NextMarker",
            description="If <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value you can use for the <code>Marker</code> request parameter to continue listing your origin access identities where they left off. ",
        ),
    ] = None
    """
    If <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value you can use for the <code>Marker</code> request parameter to continue listing your origin access identities where they left off. 
    """

    max_items: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="MaxItems"),
        pydantic.Field(
            alias="MaxItems",
            description="The maximum number of origin access identities you want in the response body. ",
        ),
    ]
    """
    The maximum number of origin access identities you want in the response body. 
    """

    is_truncated: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="IsTruncated"),
        pydantic.Field(
            alias="IsTruncated",
            description="A flag that indicates whether more origin access identities remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more items in the list.",
        ),
    ]
    """
    A flag that indicates whether more origin access identities remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more items in the list.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity",
            description="The number of CloudFront origin access identities that were created by the current AWS account. ",
        ),
    ]
    """
    The number of CloudFront origin access identities that were created by the current AWS account. 
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[CloudFrontOriginAccessIdentityListItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description="A complex type that contains one <code>CloudFrontOriginAccessIdentitySummary</code> element for each origin access identity that was created by the current AWS account.",
        ),
    ] = None
    """
    A complex type that contains one <code>CloudFrontOriginAccessIdentitySummary</code> element for each origin access identity that was created by the current AWS account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
