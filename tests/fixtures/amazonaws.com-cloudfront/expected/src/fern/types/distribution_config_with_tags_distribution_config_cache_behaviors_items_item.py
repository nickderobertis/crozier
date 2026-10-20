

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from ..core.xml_utilities import (
    XmlChild,
    XmlComment,
    XmlContent,
    XmlElement,
    XmlNode,
    build_xml_model,
    extra_xml_attributes,
    order_xml_content,
    parse_xml,
    serialize_xml_element,
    xml_child,
    xml_content,
)
from .allowed_methods import AllowedMethods
from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_forwarded_values import (
    DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValues,
)
from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_lambda_function_associations import (
    DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations,
)
from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_trusted_signers import (
    DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
)
from .distribution_config_with_tags_distribution_config_cache_behaviors_items_item_viewer_protocol_policy import (
    DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
)


class DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem(UniversalBaseModel):
    """
    <p>A complex type that describes how CloudFront processes requests.</p> <p>You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to distribute objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.</p> <p>For the current limit on the number of cache behaviors that you can add to a distribution, see <a href="http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront">Amazon CloudFront Limits</a> in the <i>AWS General Reference</i>.</p> <p>If you don't want to specify any cache behaviors, include only an empty <code>CacheBehaviors</code> element. Don't include an empty <code>CacheBehavior</code> element, or CloudFront returns a <code>MalformedXML</code> error.</p> <p>To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty <code>CacheBehaviors</code> element.</p> <p>To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.</p> <p>For more information about cache behaviors, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior">Cache Behaviors</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
    """

    path_pattern: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="PathPattern"),
        pydantic.Field(
            alias="PathPattern",
            description='<p>The pattern (for example, <code>images/*.jpg</code>) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.</p> <note> <p>You can optionally include a slash (<code>/</code>) at the beginning of the path pattern. For example, <code>/images/*.jpg</code>. CloudFront behavior is the same with or without the leading <code>/</code>.</p> </note> <p>The path pattern for the default cache behavior is <code>*</code> and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesPathPattern">Path Pattern</a> in the <i> Amazon CloudFront Developer Guide</i>.</p>',
        ),
    ]
    """
    <p>The pattern (for example, <code>images/*.jpg</code>) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.</p> <note> <p>You can optionally include a slash (<code>/</code>) at the beginning of the path pattern. For example, <code>/images/*.jpg</code>. CloudFront behavior is the same with or without the leading <code>/</code>.</p> </note> <p>The path pattern for the default cache behavior is <code>*</code> and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesPathPattern">Path Pattern</a> in the <i> Amazon CloudFront Developer Guide</i>.</p>
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
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemForwardedValues,
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
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemTrustedSigners,
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
        DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemViewerProtocolPolicy,
        FieldMetadata(alias="ViewerProtocolPolicy"),
        pydantic.Field(
            alias="ViewerProtocolPolicy",
            description='<p>The protocol that viewers can use to access the files in the origin specified by <code>TargetOriginId</code> when a request matches the path pattern in <code>PathPattern</code>. You can specify the following options:</p> <ul> <li> <p> <code>allow-all</code>: Viewers can use HTTP or HTTPS.</p> </li> <li> <p> <code>redirect-to-https</code>: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL. </p> </li> <li> <p> <code>https-only</code>: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden). </p> </li> </ul> <p>For more information about requiring the HTTPS protocol, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html">Using an HTTPS Connection to Access Your Objects</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <note> <p>The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects\' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note>',
        ),
    ]
    """
    <p>The protocol that viewers can use to access the files in the origin specified by <code>TargetOriginId</code> when a request matches the path pattern in <code>PathPattern</code>. You can specify the following options:</p> <ul> <li> <p> <code>allow-all</code>: Viewers can use HTTP or HTTPS.</p> </li> <li> <p> <code>redirect-to-https</code>: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL. </p> </li> <li> <p> <code>https-only</code>: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden). </p> </li> </ul> <p>For more information about requiring the HTTPS protocol, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecureConnections.html">Using an HTTPS Connection to Access Your Objects</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <note> <p>The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note>
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
        typing.Optional[int],
        FieldMetadata(alias="MaxTTL"),
        pydantic.Field(
            alias="MaxTTL",
            description='The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as <code>Cache-Control max-age</code>, <code>Cache-Control s-maxage</code>, and <code>Expires</code> to objects. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.',
        ),
    ] = None
    """
    The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as <code>Cache-Control max-age</code>, <code>Cache-Control s-maxage</code>, and <code>Expires</code> to objects. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Specifying How Long Objects and Errors Stay in a CloudFront Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.
    """

    compress: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Compress"),
        pydantic.Field(
            alias="Compress",
            description='Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html">Serving Compressed Files</a> in the <i>Amazon CloudFront Developer Guide</i>.',
        ),
    ] = None
    """
    Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html">Serving Compressed Files</a> in the <i>Amazon CloudFront Developer Guide</i>.
    """

    lambda_function_associations: typing_extensions.Annotated[
        typing.Optional[DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItemLambdaFunctionAssociations],
        FieldMetadata(alias="LambdaFunctionAssociations"),
        pydantic.Field(
            alias="LambdaFunctionAssociations",
            description="A complex type that contains zero or more Lambda function associations for a cache behavior.",
        ),
    ] = None
    """
    A complex type that contains zero or more Lambda function associations for a cache behavior.
    """

    _content: typing.List[XmlContent] = pydantic.PrivateAttr(default_factory=list)
    _comments_before: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)
    _comments_after: typing.List[XmlComment] = pydantic.PrivateAttr(default_factory=list)

    def to_xml(self, *, xml_declaration: bool = True) -> str:
        """
        Serializes this object as a `<CacheBehavior>` XML element, prefixed with the XML declaration unless `xml_declaration` is False.
        """
        return serialize_xml_element(
            name="CacheBehavior",
            attributes=[
                *extra_xml_attributes(self),
            ],
            children=[
                XmlChild(name="PathPattern", value=self.path_pattern),
                XmlChild(name="TargetOriginId", value=self.target_origin_id),
                XmlChild(name="ForwardedValues", value=self.forwarded_values),
                XmlChild(name="TrustedSigners", value=self.trusted_signers),
                XmlChild(name="ViewerProtocolPolicy", value=self.viewer_protocol_policy),
                XmlChild(name="MinTTL", value=self.min_ttl),
                XmlChild(name="AllowedMethods", value=self.allowed_methods),
                XmlChild(name="SmoothStreaming", value=self.smooth_streaming),
                XmlChild(name="DefaultTTL", value=self.default_ttl),
                XmlChild(name="MaxTTL", value=self.max_ttl),
                XmlChild(name="Compress", value=self.compress),
                XmlChild(name="LambdaFunctionAssociations", value=self.lambda_function_associations),
            ],
            content=order_xml_content(self._content),
            comments_before=self._comments_before,
            comments_after=self._comments_after,
            xml_declaration=xml_declaration,
        )

    def __str__(self) -> str:
        return self.to_xml()

    @classmethod
    def from_xml(
        cls, xml: typing.Union[str, XmlNode]
    ) -> DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem:
        """
        Parses a `<CacheBehavior>` XML element from a document string or a parsed node.

        Raises `ValueError` for malformed XML, an unexpected root element or invalid values. Unknown attributes are kept as extra attributes; text segments and child elements (declared or not) are preserved in document order.
        """
        node = parse_xml(xml, "CacheBehavior")
        content = xml_content(
            node,
            {},
            skip={
                "PathPattern",
                "TargetOriginId",
                "ForwardedValues",
                "TrustedSigners",
                "ViewerProtocolPolicy",
                "MinTTL",
                "AllowedMethods",
                "SmoothStreaming",
                "DefaultTTL",
                "MaxTTL",
                "Compress",
                "LambdaFunctionAssociations",
            },
        )
        model = build_xml_model(
            cls,
            dict(
                path_pattern=xml_child(node, {"PathPattern": str}),
                target_origin_id=xml_child(node, {"TargetOriginId": str}),
                forwarded_values=xml_child(node, {"ForwardedValues": str}),
                trusted_signers=xml_child(node, {"TrustedSigners": str}),
                viewer_protocol_policy=xml_child(node, {"ViewerProtocolPolicy": str}),
                min_ttl=xml_child(node, {"MinTTL": str}),
                allowed_methods=xml_child(node, {"AllowedMethods": str}),
                smooth_streaming=xml_child(node, {"SmoothStreaming": str}),
                default_ttl=xml_child(node, {"DefaultTTL": str}),
                max_ttl=xml_child(node, {"MaxTTL": str}),
                compress=xml_child(node, {"Compress": str}),
                lambda_function_associations=xml_child(node, {"LambdaFunctionAssociations": str}),
            ),
            node,
            (),
        )
        model._content[:] = content
        return model

    def add_child(self, child: XmlElement) -> DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem:
        """
        Appends an arbitrary child element (one the schema does not define) after the content added so far and returns this element.
        """
        self._content.append(child)
        return self

    def add_text(self, text: str) -> DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem:
        """
        Appends a text segment after the children added so far and returns this element, so text and child elements can be interleaved.
        """
        self._content.append(text)
        return self

    def comment(self, text: str) -> DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem:
        """
        Appends an XML comment (`<!--text-->`) inside this element, after the content added so far, and returns this element.
        """
        self._content.append(XmlComment(text))
        return self

    def comment_before(self, text: str) -> DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem:
        """
        Adds an XML comment rendered immediately before this element (as a sibling in its parent, or before the root element) and returns this element.
        """
        self._comments_before.append(XmlComment(text))
        return self

    def comment_after(self, text: str) -> DistributionConfigWithTagsDistributionConfigCacheBehaviorsItemsItem:
        """
        Adds an XML comment rendered immediately after this element (as a sibling in its parent, or after the root element) and returns this element.
        """
        self._comments_after.append(XmlComment(text))
        return self

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            copy_on_model_validation = "none"
            extra = pydantic.Extra.allow
