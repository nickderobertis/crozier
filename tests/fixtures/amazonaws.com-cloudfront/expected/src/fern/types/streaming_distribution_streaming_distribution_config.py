

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .streaming_distribution_streaming_distribution_config_aliases import (
    StreamingDistributionStreamingDistributionConfigAliases,
)
from .streaming_distribution_streaming_distribution_config_logging import (
    StreamingDistributionStreamingDistributionConfigLogging,
)
from .streaming_distribution_streaming_distribution_config_price_class import (
    StreamingDistributionStreamingDistributionConfigPriceClass,
)
from .streaming_distribution_streaming_distribution_config_s3origin import (
    StreamingDistributionStreamingDistributionConfigS3Origin,
)
from .streaming_distribution_streaming_distribution_config_trusted_signers import (
    StreamingDistributionStreamingDistributionConfigTrustedSigners,
)


class StreamingDistributionStreamingDistributionConfig(UniversalBaseModel):
    """
    The current configuration information for the RTMP distribution.
    """

    caller_reference: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallerReference"),
        pydantic.Field(
            alias="CallerReference",
            description="A unique number that ensures that the request can't be replayed. If the <code>CallerReference</code> is new (no matter the content of the <code>StreamingDistributionConfig</code> object), a new streaming distribution is created. If the <code>CallerReference</code> is a value that you already sent in a previous request to create a streaming distribution, and the content of the <code>StreamingDistributionConfig</code> is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the <code>CallerReference</code> is a value that you already sent in a previous request to create a streaming distribution but the content of the <code>StreamingDistributionConfig</code> is different from the original request, CloudFront returns a <code>DistributionAlreadyExists</code> error. ",
        ),
    ]
    """
    A unique number that ensures that the request can't be replayed. If the <code>CallerReference</code> is new (no matter the content of the <code>StreamingDistributionConfig</code> object), a new streaming distribution is created. If the <code>CallerReference</code> is a value that you already sent in a previous request to create a streaming distribution, and the content of the <code>StreamingDistributionConfig</code> is identical to the original request (ignoring white space), the response includes the same information returned to the original request. If the <code>CallerReference</code> is a value that you already sent in a previous request to create a streaming distribution but the content of the <code>StreamingDistributionConfig</code> is different from the original request, CloudFront returns a <code>DistributionAlreadyExists</code> error. 
    """

    s3origin: typing_extensions.Annotated[
        StreamingDistributionStreamingDistributionConfigS3Origin,
        FieldMetadata(alias="S3Origin"),
        pydantic.Field(
            alias="S3Origin",
            description="A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution. ",
        ),
    ]
    """
    A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution. 
    """

    aliases: typing_extensions.Annotated[
        typing.Optional[StreamingDistributionStreamingDistributionConfigAliases],
        FieldMetadata(alias="Aliases"),
        pydantic.Field(
            alias="Aliases",
            description="A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution. ",
        ),
    ] = None
    """
    A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution. 
    """

    comment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Comment"),
        pydantic.Field(
            alias="Comment", description="Any comments you want to include about the streaming distribution. "
        ),
    ]
    """
    Any comments you want to include about the streaming distribution. 
    """

    logging: typing_extensions.Annotated[
        typing.Optional[StreamingDistributionStreamingDistributionConfigLogging],
        FieldMetadata(alias="Logging"),
        pydantic.Field(
            alias="Logging",
            description="A complex type that controls whether access logs are written for the streaming distribution. ",
        ),
    ] = None
    """
    A complex type that controls whether access logs are written for the streaming distribution. 
    """

    trusted_signers: typing_extensions.Annotated[
        StreamingDistributionStreamingDistributionConfigTrustedSigners,
        FieldMetadata(alias="TrustedSigners"),
        pydantic.Field(
            alias="TrustedSigners",
            description='A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>. ',
        ),
    ]
    """
    A complex type that specifies any AWS accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>. 
    """

    price_class: typing_extensions.Annotated[
        typing.Optional[StreamingDistributionStreamingDistributionConfigPriceClass],
        FieldMetadata(alias="PriceClass"),
        pydantic.Field(
            alias="PriceClass",
            description="A complex type that contains information about price class for this streaming distribution. ",
        ),
    ] = None
    """
    A complex type that contains information about price class for this streaming distribution. 
    """

    enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Enabled"),
        pydantic.Field(
            alias="Enabled",
            description="Whether the streaming distribution is enabled to accept user requests for content.",
        ),
    ]
    """
    Whether the streaming distribution is enabled to accept user requests for content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
