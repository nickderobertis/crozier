

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfigS3Origin(
    UniversalBaseModel
):
    """
    A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.
    """

    domain_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DomainName"),
        pydantic.Field(alias="DomainName", description="The DNS name of the Amazon S3 origin. "),
    ]
    """
    The DNS name of the Amazon S3 origin. 
    """

    origin_access_identity: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="OriginAccessIdentity"),
        pydantic.Field(
            alias="OriginAccessIdentity",
            description='<p>The CloudFront origin access identity to associate with the RTMP distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.</p> <p>If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty <code>OriginAccessIdentity</code> element.</p> <p>To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty <code>OriginAccessIdentity</code> element.</p> <p>To replace the origin access identity, update the distribution configuration and specify the new origin access identity.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html">Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content</a> in the <i>Amazon Amazon CloudFront Developer Guide</i>.</p>',
        ),
    ]
    """
    <p>The CloudFront origin access identity to associate with the RTMP distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.</p> <p>If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty <code>OriginAccessIdentity</code> element.</p> <p>To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty <code>OriginAccessIdentity</code> element.</p> <p>To replace the origin access identity, update the distribution configuration and specify the new origin access identity.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html">Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content</a> in the <i>Amazon Amazon CloudFront Developer Guide</i>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
