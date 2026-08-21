

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_distribution_with_tags_result_distribution_active_trusted_signers import (
    CreateDistributionWithTagsResultDistributionActiveTrustedSigners,
)
from .create_distribution_with_tags_result_distribution_distribution_config import (
    CreateDistributionWithTagsResultDistributionDistributionConfig,
)


class CreateDistributionWithTagsResultDistribution(UniversalBaseModel):
    """
    The distribution's information.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id", description="The identifier for the distribution. For example: <code>EDFDVBD632BHDS5</code>. "
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
            description="This response element indicates the current status of the distribution. When the status is <code>Deployed</code>, the distribution's information is fully propagated to all CloudFront edge locations. ",
        ),
    ]
    """
    This response element indicates the current status of the distribution. When the status is <code>Deployed</code>, the distribution's information is fully propagated to all CloudFront edge locations. 
    """

    last_modified_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="LastModifiedTime"),
        pydantic.Field(alias="LastModifiedTime", description="The date and time the distribution was last modified. "),
    ]
    """
    The date and time the distribution was last modified. 
    """

    in_progress_invalidation_batches: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="InProgressInvalidationBatches"),
        pydantic.Field(
            alias="InProgressInvalidationBatches",
            description="The number of invalidation batches currently in progress. ",
        ),
    ]
    """
    The number of invalidation batches currently in progress. 
    """

    domain_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DomainName"),
        pydantic.Field(
            alias="DomainName",
            description="The domain name corresponding to the distribution. For example: <code>d604721fxaaqy9.cloudfront.net</code>. ",
        ),
    ]
    """
    The domain name corresponding to the distribution. For example: <code>d604721fxaaqy9.cloudfront.net</code>. 
    """

    active_trusted_signers: typing_extensions.Annotated[
        CreateDistributionWithTagsResultDistributionActiveTrustedSigners,
        FieldMetadata(alias="ActiveTrustedSigners"),
        pydantic.Field(
            alias="ActiveTrustedSigners",
            description="CloudFront automatically adds this element to the response only if you've set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The <code>Signer</code> child element lists the AWS account number of the trusted signer (or an empty <code>Self</code> element if the signer is you). The <code>Signer</code> element also includes the IDs of any active key pairs associated with the trusted signer's AWS account. If no <code>KeyPairId</code> element appears for a <code>Signer</code>, that signer can't create working signed URLs.",
        ),
    ]
    """
    CloudFront automatically adds this element to the response only if you've set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The <code>Signer</code> child element lists the AWS account number of the trusted signer (or an empty <code>Self</code> element if the signer is you). The <code>Signer</code> element also includes the IDs of any active key pairs associated with the trusted signer's AWS account. If no <code>KeyPairId</code> element appears for a <code>Signer</code>, that signer can't create working signed URLs.
    """

    distribution_config: typing_extensions.Annotated[
        CreateDistributionWithTagsResultDistributionDistributionConfig,
        FieldMetadata(alias="DistributionConfig"),
        pydantic.Field(
            alias="DistributionConfig",
            description="The current configuration information for the distribution. Send a <code>GET</code> request to the <code>/<i>CloudFront API version</i>/distribution ID/config</code> resource.",
        ),
    ]
    """
    The current configuration information for the distribution. Send a <code>GET</code> request to the <code>/<i>CloudFront API version</i>/distribution ID/config</code> resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
