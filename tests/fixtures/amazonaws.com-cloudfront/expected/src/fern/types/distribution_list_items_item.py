

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .distribution_list_items_item_aliases import DistributionListItemsItemAliases
from .distribution_list_items_item_cache_behaviors import DistributionListItemsItemCacheBehaviors
from .distribution_list_items_item_custom_error_responses import DistributionListItemsItemCustomErrorResponses
from .distribution_list_items_item_default_cache_behavior import DistributionListItemsItemDefaultCacheBehavior
from .distribution_list_items_item_http_version import DistributionListItemsItemHttpVersion
from .distribution_list_items_item_origins import DistributionListItemsItemOrigins
from .price_class import PriceClass
from .restrictions import Restrictions
from .viewer_certificate import ViewerCertificate


class DistributionListItemsItem(UniversalBaseModel):
    """
    A summary of the information about a CloudFront distribution.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id", description="The identifier for the distribution. For example: <code>EDFDVBD632BHDS5</code>."
        ),
    ]
    """
    The identifier for the distribution. For example: <code>EDFDVBD632BHDS5</code>.
    """

    arn: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ARN"),
        pydantic.Field(
            alias="ARN",
            description="The ARN (Amazon Resource Name) for the distribution. For example: <code>arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5</code>, where <code>123456789012</code> is your AWS account ID.",
        ),
    ]
    """
    The ARN (Amazon Resource Name) for the distribution. For example: <code>arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5</code>, where <code>123456789012</code> is your AWS account ID.
    """

    status: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description="The current status of the distribution. When the status is <code>Deployed</code>, the distribution's information is propagated to all CloudFront edge locations.",
        ),
    ]
    """
    The current status of the distribution. When the status is <code>Deployed</code>, the distribution's information is propagated to all CloudFront edge locations.
    """

    last_modified_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="LastModifiedTime"),
        pydantic.Field(alias="LastModifiedTime", description="The date and time the distribution was last modified."),
    ]
    """
    The date and time the distribution was last modified.
    """

    domain_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DomainName"),
        pydantic.Field(
            alias="DomainName",
            description="The domain name that corresponds to the distribution. For example: <code>d604721fxaaqy9.cloudfront.net</code>.",
        ),
    ]
    """
    The domain name that corresponds to the distribution. For example: <code>d604721fxaaqy9.cloudfront.net</code>.
    """

    aliases: typing_extensions.Annotated[
        DistributionListItemsItemAliases,
        FieldMetadata(alias="Aliases"),
        pydantic.Field(
            alias="Aliases",
            description="A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.",
        ),
    ]
    """
    A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
    """

    origins: typing_extensions.Annotated[
        DistributionListItemsItemOrigins,
        FieldMetadata(alias="Origins"),
        pydantic.Field(
            alias="Origins", description="A complex type that contains information about origins for this distribution."
        ),
    ]
    """
    A complex type that contains information about origins for this distribution.
    """

    default_cache_behavior: typing_extensions.Annotated[
        DistributionListItemsItemDefaultCacheBehavior,
        FieldMetadata(alias="DefaultCacheBehavior"),
        pydantic.Field(
            alias="DefaultCacheBehavior",
            description="A complex type that describes the default cache behavior if you do not specify a <code>CacheBehavior</code> element or if files don't match any of the values of <code>PathPattern</code> in <code>CacheBehavior</code> elements. You must create exactly one default cache behavior.",
        ),
    ]
    """
    A complex type that describes the default cache behavior if you do not specify a <code>CacheBehavior</code> element or if files don't match any of the values of <code>PathPattern</code> in <code>CacheBehavior</code> elements. You must create exactly one default cache behavior.
    """

    cache_behaviors: typing_extensions.Annotated[
        DistributionListItemsItemCacheBehaviors,
        FieldMetadata(alias="CacheBehaviors"),
        pydantic.Field(
            alias="CacheBehaviors",
            description="A complex type that contains zero or more <code>CacheBehavior</code> elements.",
        ),
    ]
    """
    A complex type that contains zero or more <code>CacheBehavior</code> elements.
    """

    custom_error_responses: typing_extensions.Annotated[
        DistributionListItemsItemCustomErrorResponses,
        FieldMetadata(alias="CustomErrorResponses"),
        pydantic.Field(
            alias="CustomErrorResponses",
            description="A complex type that contains zero or more <code>CustomErrorResponses</code> elements.",
        ),
    ]
    """
    A complex type that contains zero or more <code>CustomErrorResponses</code> elements.
    """

    comment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Comment"),
        pydantic.Field(
            alias="Comment", description="The comment originally specified when this distribution was created."
        ),
    ]
    """
    The comment originally specified when this distribution was created.
    """

    price_class: typing_extensions.Annotated[
        PriceClass, FieldMetadata(alias="PriceClass"), pydantic.Field(alias="PriceClass")
    ]
    enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Enabled"),
        pydantic.Field(
            alias="Enabled", description="Whether the distribution is enabled to accept user requests for content."
        ),
    ]
    """
    Whether the distribution is enabled to accept user requests for content.
    """

    viewer_certificate: typing_extensions.Annotated[
        ViewerCertificate, FieldMetadata(alias="ViewerCertificate"), pydantic.Field(alias="ViewerCertificate")
    ]
    restrictions: typing_extensions.Annotated[
        Restrictions, FieldMetadata(alias="Restrictions"), pydantic.Field(alias="Restrictions")
    ]
    web_acl_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="WebACLId"),
        pydantic.Field(alias="WebACLId", description="The Web ACL Id (if any) associated with the distribution."),
    ]
    """
    The Web ACL Id (if any) associated with the distribution.
    """

    http_version: typing_extensions.Annotated[
        DistributionListItemsItemHttpVersion,
        FieldMetadata(alias="HttpVersion"),
        pydantic.Field(
            alias="HttpVersion",
            description=" Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is <code>http2</code>. Viewers that don't support <code>HTTP/2</code> will automatically use an earlier version.",
        ),
    ]
    """
     Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is <code>http2</code>. Viewers that don't support <code>HTTP/2</code> will automatically use an earlier version.
    """

    is_ipv6enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="IsIPV6Enabled"),
        pydantic.Field(
            alias="IsIPV6Enabled",
            description="Whether CloudFront responds to IPv6 DNS requests with an IPv6 address for your distribution.",
        ),
    ]
    """
    Whether CloudFront responds to IPv6 DNS requests with an IPv6 address for your distribution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
