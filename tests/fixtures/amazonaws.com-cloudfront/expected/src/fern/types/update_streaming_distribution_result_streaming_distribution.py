

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .string import String
from .update_streaming_distribution_result_streaming_distribution_active_trusted_signers import (
    UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSigners,
)
from .update_streaming_distribution_result_streaming_distribution_streaming_distribution_config import (
    UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfig,
)


class UpdateStreamingDistributionResultStreamingDistribution(UniversalBaseModel):
    """
    The streaming distribution's information.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id",
            description="The identifier for the RTMP distribution. For example: <code>EGTXBD79EXAMPLE</code>.",
        ),
    ]
    """
    The identifier for the RTMP distribution. For example: <code>EGTXBD79EXAMPLE</code>.
    """

    arn: typing_extensions.Annotated[String, FieldMetadata(alias="ARN"), pydantic.Field(alias="ARN")]
    status: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description="The current status of the RTMP distribution. When the status is <code>Deployed</code>, the distribution's information is propagated to all CloudFront edge locations.",
        ),
    ]
    """
    The current status of the RTMP distribution. When the status is <code>Deployed</code>, the distribution's information is propagated to all CloudFront edge locations.
    """

    last_modified_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastModifiedTime"),
        pydantic.Field(
            alias="LastModifiedTime", description="The date and time that the distribution was last modified. "
        ),
    ] = None
    """
    The date and time that the distribution was last modified. 
    """

    domain_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DomainName"),
        pydantic.Field(
            alias="DomainName",
            description="The domain name that corresponds to the streaming distribution. For example: <code>s5c39gqb8ow64r.cloudfront.net</code>. ",
        ),
    ]
    """
    The domain name that corresponds to the streaming distribution. For example: <code>s5c39gqb8ow64r.cloudfront.net</code>. 
    """

    active_trusted_signers: typing_extensions.Annotated[
        UpdateStreamingDistributionResultStreamingDistributionActiveTrustedSigners,
        FieldMetadata(alias="ActiveTrustedSigners"),
        pydantic.Field(
            alias="ActiveTrustedSigners",
            description="<p>A complex type that lists the AWS accounts, if any, that you included in the <code>TrustedSigners</code> complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.</p> <p>The <code>Signer</code> complex type lists the AWS account number of the trusted signer or <code>self</code> if the signer is the AWS account that created the distribution. The <code>Signer</code> element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer's AWS account. If no <code>KeyPairId</code> element appears for a <code>Signer</code>, that signer can't create signed URLs.</p> <p>For more information, see <a href=\"http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>. </p>",
        ),
    ]
    """
    <p>A complex type that lists the AWS accounts, if any, that you included in the <code>TrustedSigners</code> complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.</p> <p>The <code>Signer</code> complex type lists the AWS account number of the trusted signer or <code>self</code> if the signer is the AWS account that created the distribution. The <code>Signer</code> element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signer's AWS account. If no <code>KeyPairId</code> element appears for a <code>Signer</code>, that signer can't create signed URLs.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving Private Content through CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>. </p>
    """

    streaming_distribution_config: typing_extensions.Annotated[
        UpdateStreamingDistributionResultStreamingDistributionStreamingDistributionConfig,
        FieldMetadata(alias="StreamingDistributionConfig"),
        pydantic.Field(
            alias="StreamingDistributionConfig",
            description="The current configuration information for the RTMP distribution.",
        ),
    ]
    """
    The current configuration information for the RTMP distribution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
