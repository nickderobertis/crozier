

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .allowed_methods import AllowedMethods
from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_forwarded_values import (
    ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValues,
)
from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_lambda_function_associations import (
    ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations,
)
from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_trusted_signers import (
    ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorTrustedSigners,
)
from .list_distributions_by_web_acl_id_result_distribution_list_items_item_default_cache_behavior_viewer_protocol_policy import (
    ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy,
)
from .long_ import Long


class ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehavior(UniversalBaseModel):
    """
    A complex type that describes the default cache behavior if you do not specify a <code>CacheBehavior</code> element or if files don't match any of the values of <code>PathPattern</code> in <code>CacheBehavior</code> elements. You must create exactly one default cache behavior.
    """

    target_origin_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="TargetOriginId"),
        pydantic.Field(
            alias="TargetOriginId",
            description="The value of <code>ID</code> for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.",
        ),
    ]
    """
    The value of <code>ID</code> for the origin that you want CloudFront to route requests to when a request matches the path pattern either for a cache behavior or for the default cache behavior.
    """

    forwarded_values: typing_extensions.Annotated[
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorForwardedValues,
        FieldMetadata(alias="ForwardedValues"),
        pydantic.Field(
            alias="ForwardedValues",
            description="A complex type that specifies how CloudFront handles query strings and cookies.",
        ),
    ]
    """
    A complex type that specifies how CloudFront handles query strings and cookies.
    """

    trusted_signers: typing_extensions.Annotated[
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorTrustedSigners,
        FieldMetadata(alias="TrustedSigners"),
        pydantic.Field(
            alias="TrustedSigners",
            description="<p>A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.</p> <p>If you want to require signed URLs in requests for objects in the target origin that match the <code>PathPattern</code> for this cache behavior, specify <code>true</code> for <code>Enabled</code>, and specify the applicable values for <code>Quantity</code> and <code>Items</code>. For more information, see <a href=\"http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\">Serving Private Content through CloudFront</a> in the <i>Amazon Amazon CloudFront Developer Guide</i>.</p> <p>If you don't want to require signed URLs in requests for objects that match <code>PathPattern</code>, specify <code>false</code> for <code>Enabled</code> and <code>0</code> for <code>Quantity</code>. Omit <code>Items</code>.</p> <p>To add, change, or remove one or more trusted signers, change <code>Enabled</code> to <code>true</code> (if it's currently <code>false</code>), change <code>Quantity</code> as applicable, and specify all of the trusted signers that you want to include in the updated distribution.</p>",
        ),
    ]
    """
    <p>A complex type that specifies the AWS accounts, if any, that you want to allow to create signed URLs for private content.</p> <p>If you want to require signed URLs in requests for objects in the target origin that match the <code>PathPattern</code> for this cache behavior, specify <code>true</code> for <code>Enabled</code>, and specify the applicable values for <code>Quantity</code> and <code>Items</code>. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon Amazon CloudFront Developer Guide</i>.</p> <p>If you don't want to require signed URLs in requests for objects that match <code>PathPattern</code>, specify <code>false</code> for <code>Enabled</code> and <code>0</code> for <code>Quantity</code>. Omit <code>Items</code>.</p> <p>To add, change, or remove one or more trusted signers, change <code>Enabled</code> to <code>true</code> (if it's currently <code>false</code>), change <code>Quantity</code> as applicable, and specify all of the trusted signers that you want to include in the updated distribution.</p>
    """

    viewer_protocol_policy: typing_extensions.Annotated[
        ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorViewerProtocolPolicy,
        FieldMetadata(alias="ViewerProtocolPolicy"),
        pydantic.Field(
            alias="ViewerProtocolPolicy",
            description='<p>The protocol that viewers can use to access the files in the origin specified by <code>TargetOriginId</code> when a request matches the path pattern in <code>PathPattern</code>. You can specify the following options:</p> <ul> <li> <p> <code>allow-all</code>: Viewers can use HTTP or HTTPS.</p> </li> <li> <p> <code>redirect-to-https</code>: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.</p> </li> <li> <p> <code>https-only</code>: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).</p> </li> </ul> <p>For more information about requiring the HTTPS protocol, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html">Using an HTTPS Connection to Access Your Objects</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <note> <p>The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note>',
        ),
    ]
    """
    <p>The protocol that viewers can use to access the files in the origin specified by <code>TargetOriginId</code> when a request matches the path pattern in <code>PathPattern</code>. You can specify the following options:</p> <ul> <li> <p> <code>allow-all</code>: Viewers can use HTTP or HTTPS.</p> </li> <li> <p> <code>redirect-to-https</code>: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.</p> </li> <li> <p> <code>https-only</code>: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).</p> </li> </ul> <p>For more information about requiring the HTTPS protocol, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html">Using an HTTPS Connection to Access Your Objects</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <note> <p>The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note>
    """

    min_ttl: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="MinTTL"),
        pydantic.Field(
            alias="MinTTL",
            description='<p>The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon Amazon CloudFront Developer Guide</i>.</p> <p>You must specify <code>0</code> for <code>MinTTL</code> if you configure CloudFront to forward all headers to your origin (under <code>Headers</code>, if you specify <code>1</code> for <code>Quantity</code> and <code>*</code> for <code>Name</code>).</p>',
        ),
    ]
    """
    <p>The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon Amazon CloudFront Developer Guide</i>.</p> <p>You must specify <code>0</code> for <code>MinTTL</code> if you configure CloudFront to forward all headers to your origin (under <code>Headers</code>, if you specify <code>1</code> for <code>Quantity</code> and <code>*</code> for <code>Name</code>).</p>
    """

    allowed_methods: typing_extensions.Annotated[
        typing.Optional[AllowedMethods], FieldMetadata(alias="AllowedMethods"), pydantic.Field(alias="AllowedMethods")
    ] = None
    smooth_streaming: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="SmoothStreaming"),
        pydantic.Field(
            alias="SmoothStreaming",
            description="Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify <code>true</code>; if not, specify <code>false</code>. If you specify <code>true</code> for <code>SmoothStreaming</code>, you can still distribute other content using this cache behavior if the content matches the value of <code>PathPattern</code>. ",
        ),
    ] = None
    """
    Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify <code>true</code>; if not, specify <code>false</code>. If you specify <code>true</code> for <code>SmoothStreaming</code>, you can still distribute other content using this cache behavior if the content matches the value of <code>PathPattern</code>. 
    """

    default_ttl: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="DefaultTTL"),
        pydantic.Field(
            alias="DefaultTTL",
            description='The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as <code>Cache-Control max-age</code>, <code>Cache-Control s-maxage</code>, and <code>Expires</code> to objects. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.',
        ),
    ] = None
    """
    The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as <code>Cache-Control max-age</code>, <code>Cache-Control s-maxage</code>, and <code>Expires</code> to objects. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.
    """

    max_ttl: typing_extensions.Annotated[
        typing.Optional[Long], FieldMetadata(alias="MaxTTL"), pydantic.Field(alias="MaxTTL")
    ] = None
    compress: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Compress"),
        pydantic.Field(
            alias="Compress",
            description='Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify <code>true</code>; if not, specify <code>false</code>. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html">Serving Compressed Files</a> in the <i>Amazon CloudFront Developer Guide</i>.',
        ),
    ] = None
    """
    Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify <code>true</code>; if not, specify <code>false</code>. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html">Serving Compressed Files</a> in the <i>Amazon CloudFront Developer Guide</i>.
    """

    lambda_function_associations: typing_extensions.Annotated[
        typing.Optional[
            ListDistributionsByWebAclIdResultDistributionListItemsItemDefaultCacheBehaviorLambdaFunctionAssociations
        ],
        FieldMetadata(alias="LambdaFunctionAssociations"),
        pydantic.Field(
            alias="LambdaFunctionAssociations",
            description="A complex type that contains zero or more Lambda function associations for a cache behavior.",
        ),
    ] = None
    """
    A complex type that contains zero or more Lambda function associations for a cache behavior.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
