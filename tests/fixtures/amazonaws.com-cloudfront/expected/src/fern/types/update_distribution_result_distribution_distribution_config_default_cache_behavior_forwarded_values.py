

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_cookies import (
    UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
)
from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_headers import (
    UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders,
)
from .update_distribution_result_distribution_distribution_config_default_cache_behavior_forwarded_values_query_string_cache_keys import (
    UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys,
)


class UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValues(UniversalBaseModel):
    """
    A complex type that specifies how CloudFront handles query strings and cookies.
    """

    query_string: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="QueryString"),
        pydantic.Field(
            alias="QueryString",
            description="<p>Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of <code>QueryString</code> and on the values that you specify for <code>QueryStringCacheKeys</code>, if any:</p> <p>If you specify true for <code>QueryString</code> and you don't specify any values for <code>QueryStringCacheKeys</code>, CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.</p> <p>If you specify true for <code>QueryString</code> and you specify one or more values for <code>QueryStringCacheKeys</code>, CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.</p> <p>If you specify false for <code>QueryString</code>, CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.</p> <p>For more information, see <a href=\"http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html\">Configuring CloudFront to Cache Based on Query String Parameters</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>",
        ),
    ]
    """
    <p>Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of <code>QueryString</code> and on the values that you specify for <code>QueryStringCacheKeys</code>, if any:</p> <p>If you specify true for <code>QueryString</code> and you don't specify any values for <code>QueryStringCacheKeys</code>, CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.</p> <p>If you specify true for <code>QueryString</code> and you specify one or more values for <code>QueryStringCacheKeys</code>, CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.</p> <p>If you specify false for <code>QueryString</code>, CloudFront doesn't forward any query string parameters to the origin, and doesn't cache based on query string parameters.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html">Configuring CloudFront to Cache Based on Query String Parameters</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>
    """

    cookies: typing_extensions.Annotated[
        UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesCookies,
        FieldMetadata(alias="Cookies"),
        pydantic.Field(
            alias="Cookies",
            description='A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html">How CloudFront Forwards, Caches, and Logs Cookies</a> in the <i>Amazon CloudFront Developer Guide</i>.',
        ),
    ]
    """
    A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html">How CloudFront Forwards, Caches, and Logs Cookies</a> in the <i>Amazon CloudFront Developer Guide</i>.
    """

    headers: typing_extensions.Annotated[
        typing.Optional[
            UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesHeaders
        ],
        FieldMetadata(alias="Headers"),
        pydantic.Field(
            alias="Headers",
            description="A complex type that specifies the <code>Headers</code>, if any, that you want CloudFront to vary upon for this cache behavior. ",
        ),
    ] = None
    """
    A complex type that specifies the <code>Headers</code>, if any, that you want CloudFront to vary upon for this cache behavior. 
    """

    query_string_cache_keys: typing_extensions.Annotated[
        typing.Optional[
            UpdateDistributionResultDistributionDistributionConfigDefaultCacheBehaviorForwardedValuesQueryStringCacheKeys
        ],
        FieldMetadata(alias="QueryStringCacheKeys"),
        pydantic.Field(
            alias="QueryStringCacheKeys",
            description="A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.",
        ),
    ] = None
    """
    A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
