

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .distribution_config_with_tags_distribution_config_aliases import (
    DistributionConfigWithTagsDistributionConfigAliases,
)
from .distribution_config_with_tags_distribution_config_cache_behaviors import (
    DistributionConfigWithTagsDistributionConfigCacheBehaviors,
)
from .distribution_config_with_tags_distribution_config_custom_error_responses import (
    DistributionConfigWithTagsDistributionConfigCustomErrorResponses,
)
from .distribution_config_with_tags_distribution_config_default_cache_behavior import (
    DistributionConfigWithTagsDistributionConfigDefaultCacheBehavior,
)
from .distribution_config_with_tags_distribution_config_http_version import (
    DistributionConfigWithTagsDistributionConfigHttpVersion,
)
from .distribution_config_with_tags_distribution_config_logging import (
    DistributionConfigWithTagsDistributionConfigLogging,
)
from .distribution_config_with_tags_distribution_config_origins import (
    DistributionConfigWithTagsDistributionConfigOrigins,
)
from .distribution_config_with_tags_distribution_config_price_class import (
    DistributionConfigWithTagsDistributionConfigPriceClass,
)
from .restrictions import Restrictions
from .viewer_certificate import ViewerCertificate


class DistributionConfigWithTagsDistributionConfig(UniversalBaseModel):
    """
    A distribution configuration.
    """

    caller_reference: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallerReference"),
        pydantic.Field(
            alias="CallerReference",
            description="<p>A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.</p> <p>If the value of <code>CallerReference</code> is new (regardless of the content of the <code>DistributionConfig</code> object), CloudFront creates a new distribution.</p> <p>If <code>CallerReference</code> is a value you already sent in a previous request to create a distribution, and if the content of the <code>DistributionConfig</code> is identical to the original request (ignoring white space), CloudFront returns the same the response that it returned to the original request.</p> <p>If <code>CallerReference</code> is a value you already sent in a previous request to create a distribution but the content of the <code>DistributionConfig</code> is different from the original request, CloudFront returns a <code>DistributionAlreadyExists</code> error.</p>",
        ),
    ]
    """
    <p>A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.</p> <p>If the value of <code>CallerReference</code> is new (regardless of the content of the <code>DistributionConfig</code> object), CloudFront creates a new distribution.</p> <p>If <code>CallerReference</code> is a value you already sent in a previous request to create a distribution, and if the content of the <code>DistributionConfig</code> is identical to the original request (ignoring white space), CloudFront returns the same the response that it returned to the original request.</p> <p>If <code>CallerReference</code> is a value you already sent in a previous request to create a distribution but the content of the <code>DistributionConfig</code> is different from the original request, CloudFront returns a <code>DistributionAlreadyExists</code> error.</p>
    """

    aliases: typing_extensions.Annotated[
        typing.Optional[DistributionConfigWithTagsDistributionConfigAliases],
        FieldMetadata(alias="Aliases"),
        pydantic.Field(
            alias="Aliases",
            description="A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.",
        ),
    ] = None
    """
    A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.
    """

    default_root_object: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DefaultRootObject"),
        pydantic.Field(
            alias="DefaultRootObject",
            description='<p>The object that you want CloudFront to request from your origin (for example, <code>index.html</code>) when a viewer requests the root URL for your distribution (<code>http://www.example.com</code>) instead of an object in your distribution (<code>http://www.example.com/product-description.html</code>). Specifying a default root object avoids exposing the contents of your distribution.</p> <p>Specify only the object name, for example, <code>index.html</code>. Do not add a <code>/</code> before the object name.</p> <p>If you don\'t want to specify a default root object when you create a distribution, include an empty <code>DefaultRootObject</code> element.</p> <p>To delete the default root object from an existing distribution, update the distribution configuration and include an empty <code>DefaultRootObject</code> element.</p> <p>To replace the default root object, update the distribution configuration and specify the new object.</p> <p>For more information about the default root object, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html">Creating a Default Root Object</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>',
        ),
    ] = None
    """
    <p>The object that you want CloudFront to request from your origin (for example, <code>index.html</code>) when a viewer requests the root URL for your distribution (<code>http://www.example.com</code>) instead of an object in your distribution (<code>http://www.example.com/product-description.html</code>). Specifying a default root object avoids exposing the contents of your distribution.</p> <p>Specify only the object name, for example, <code>index.html</code>. Do not add a <code>/</code> before the object name.</p> <p>If you don't want to specify a default root object when you create a distribution, include an empty <code>DefaultRootObject</code> element.</p> <p>To delete the default root object from an existing distribution, update the distribution configuration and include an empty <code>DefaultRootObject</code> element.</p> <p>To replace the default root object, update the distribution configuration and specify the new object.</p> <p>For more information about the default root object, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html">Creating a Default Root Object</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
    """

    origins: typing_extensions.Annotated[
        DistributionConfigWithTagsDistributionConfigOrigins,
        FieldMetadata(alias="Origins"),
        pydantic.Field(
            alias="Origins",
            description="A complex type that contains information about origins for this distribution. ",
        ),
    ]
    """
    A complex type that contains information about origins for this distribution. 
    """

    default_cache_behavior: typing_extensions.Annotated[
        DistributionConfigWithTagsDistributionConfigDefaultCacheBehavior,
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
        typing.Optional[DistributionConfigWithTagsDistributionConfigCacheBehaviors],
        FieldMetadata(alias="CacheBehaviors"),
        pydantic.Field(
            alias="CacheBehaviors",
            description="A complex type that contains zero or more <code>CacheBehavior</code> elements. ",
        ),
    ] = None
    """
    A complex type that contains zero or more <code>CacheBehavior</code> elements. 
    """

    custom_error_responses: typing_extensions.Annotated[
        typing.Optional[DistributionConfigWithTagsDistributionConfigCustomErrorResponses],
        FieldMetadata(alias="CustomErrorResponses"),
        pydantic.Field(
            alias="CustomErrorResponses",
            description='<p>A complex type that controls the following:</p> <ul> <li> <p>Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.</p> </li> <li> <p>How long CloudFront caches HTTP status codes in the 4xx and 5xx range.</p> </li> </ul> <p>For more information about custom error pages, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html">Customizing Error Responses</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>',
        ),
    ] = None
    """
    <p>A complex type that controls the following:</p> <ul> <li> <p>Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.</p> </li> <li> <p>How long CloudFront caches HTTP status codes in the 4xx and 5xx range.</p> </li> </ul> <p>For more information about custom error pages, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html">Customizing Error Responses</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
    """

    comment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Comment"),
        pydantic.Field(
            alias="Comment",
            description="<p>Any comments you want to include about the distribution.</p> <p>If you don't want to specify a comment, include an empty <code>Comment</code> element.</p> <p>To delete an existing comment, update the distribution configuration and include an empty <code>Comment</code> element.</p> <p>To add or change a comment, update the distribution configuration and specify the new comment.</p>",
        ),
    ]
    """
    <p>Any comments you want to include about the distribution.</p> <p>If you don't want to specify a comment, include an empty <code>Comment</code> element.</p> <p>To delete an existing comment, update the distribution configuration and include an empty <code>Comment</code> element.</p> <p>To add or change a comment, update the distribution configuration and specify the new comment.</p>
    """

    logging: typing_extensions.Annotated[
        typing.Optional[DistributionConfigWithTagsDistributionConfigLogging],
        FieldMetadata(alias="Logging"),
        pydantic.Field(
            alias="Logging",
            description='<p>A complex type that controls whether access logs are written for the distribution.</p> <p>For more information about logging, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html">Access Logs</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>',
        ),
    ] = None
    """
    <p>A complex type that controls whether access logs are written for the distribution.</p> <p>For more information about logging, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html">Access Logs</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
    """

    price_class: typing_extensions.Annotated[
        typing.Optional[DistributionConfigWithTagsDistributionConfigPriceClass],
        FieldMetadata(alias="PriceClass"),
        pydantic.Field(
            alias="PriceClass",
            description='<p>The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify <code>PriceClass_All</code>, CloudFront responds to requests for your objects from all CloudFront edge locations.</p> <p>If you specify a price class other than <code>PriceClass_All</code>, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.</p> <p>For more information about price classes, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html">Choosing the Price Class for a CloudFront Distribution</a> in the <i>Amazon CloudFront Developer Guide</i>. For information about CloudFront pricing, including how price classes map to CloudFront regions, see <a href="https://aws.amazon.com/cloudfront/pricing/">Amazon CloudFront Pricing</a>.</p>',
        ),
    ] = None
    """
    <p>The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify <code>PriceClass_All</code>, CloudFront responds to requests for your objects from all CloudFront edge locations.</p> <p>If you specify a price class other than <code>PriceClass_All</code>, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.</p> <p>For more information about price classes, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html">Choosing the Price Class for a CloudFront Distribution</a> in the <i>Amazon CloudFront Developer Guide</i>. For information about CloudFront pricing, including how price classes map to CloudFront regions, see <a href="https://aws.amazon.com/cloudfront/pricing/">Amazon CloudFront Pricing</a>.</p>
    """

    enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Enabled"),
        pydantic.Field(
            alias="Enabled",
            description="<p>Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket.</p> <p>If you do not want to enable logging when you create a distribution, or if you want to disable logging for an existing distribution, specify <code>false</code> for <code>Enabled</code>, and specify empty <code>Bucket</code> and <code>Prefix</code> elements.</p> <p>If you specify <code>false</code> for <code>Enabled</code> but you specify values for <code>Bucket</code> and <code>Prefix</code>, the values are automatically deleted.</p>",
        ),
    ]
    """
    <p>Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket.</p> <p>If you do not want to enable logging when you create a distribution, or if you want to disable logging for an existing distribution, specify <code>false</code> for <code>Enabled</code>, and specify empty <code>Bucket</code> and <code>Prefix</code> elements.</p> <p>If you specify <code>false</code> for <code>Enabled</code> but you specify values for <code>Bucket</code> and <code>Prefix</code>, the values are automatically deleted.</p>
    """

    viewer_certificate: typing_extensions.Annotated[
        typing.Optional[ViewerCertificate],
        FieldMetadata(alias="ViewerCertificate"),
        pydantic.Field(alias="ViewerCertificate"),
    ] = None
    restrictions: typing_extensions.Annotated[
        typing.Optional[Restrictions], FieldMetadata(alias="Restrictions"), pydantic.Field(alias="Restrictions")
    ] = None
    web_acl_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="WebACLId"),
        pydantic.Field(
            alias="WebACLId",
            description='<p>A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution.</p> <p>AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the <a href="http://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html">AWS WAF Developer Guide</a>. </p>',
        ),
    ] = None
    """
    <p>A unique identifier that specifies the AWS WAF web ACL, if any, to associate with this distribution.</p> <p>AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about AWS WAF, see the <a href="http://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html">AWS WAF Developer Guide</a>. </p>
    """

    http_version: typing_extensions.Annotated[
        typing.Optional[DistributionConfigWithTagsDistributionConfigHttpVersion],
        FieldMetadata(alias="HttpVersion"),
        pydantic.Field(
            alias="HttpVersion",
            description='<p>(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don\'t support HTTP/2 automatically use an earlier HTTP version.</p> <p>For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).</p> <p>In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for "http/2 optimization." </p>',
        ),
    ] = None
    """
    <p>(Optional) Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is http2. Viewers that don't support HTTP/2 automatically use an earlier HTTP version.</p> <p>For viewers and CloudFront to use HTTP/2, viewers must support TLS 1.2 or later, and must support Server Name Identification (SNI).</p> <p>In general, configuring CloudFront to communicate with viewers using HTTP/2 reduces latency. You can improve performance by optimizing for HTTP/2. For more information, do an Internet search for "http/2 optimization." </p>
    """

    is_ipv6enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsIPV6Enabled"),
        pydantic.Field(
            alias="IsIPV6Enabled",
            description="<p>If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify <code>true</code>. If you specify <code>false</code>, CloudFront responds to IPv6 DNS requests with the DNS response code <code>NOERROR</code> and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. </p> <p>In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you're using signed URLs or signed cookies to restrict access to your content, and if you're using a custom policy that includes the <code>IpAddress</code> parameter to restrict the IP addresses that can access your content, do not enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see <a href=\"http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-creating-signed-url-custom-policy.html\">Creating a Signed URL Using a Custom Policy</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you're using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:</p> <ul> <li> <p>You enable IPv6 for the distribution</p> </li> <li> <p>You're using alternate domain names in the URLs for your objects</p> </li> </ul> <p>For more information, see <a href=\"http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html\">Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don't need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.</p>",
        ),
    ] = None
    """
    <p>If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify <code>true</code>. If you specify <code>false</code>, CloudFront responds to IPv6 DNS requests with the DNS response code <code>NOERROR</code> and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution. </p> <p>In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you're using signed URLs or signed cookies to restrict access to your content, and if you're using a custom policy that includes the <code>IpAddress</code> parameter to restrict the IP addresses that can access your content, do not enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-creating-signed-url-custom-policy.html">Creating a Signed URL Using a Custom Policy</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you're using an Amazon Route 53 alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:</p> <ul> <li> <p>You enable IPv6 for the distribution</p> </li> <li> <p>You're using alternate domain names in the URLs for your objects</p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html">Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>If you created a CNAME resource record set, either with Amazon Route 53 or with another DNS service, you don't need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
