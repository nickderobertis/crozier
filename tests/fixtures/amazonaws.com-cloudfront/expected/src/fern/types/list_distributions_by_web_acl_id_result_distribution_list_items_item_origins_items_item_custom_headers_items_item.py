

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ListDistributionsByWebAclIdResultDistributionListItemsItemOriginsItemsItemCustomHeadersItemsItem(
    UniversalBaseModel
):
    """
    A complex type that contains <code>HeaderName</code> and <code>HeaderValue</code> elements, if any, for this distribution.
    """

    header_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="HeaderName"),
        pydantic.Field(
            alias="HeaderName",
            description='The name of a header that you want CloudFront to forward to your origin. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html">Forwarding Custom Headers to Your Origin (Web Distributions Only)</a> in the <i>Amazon Amazon CloudFront Developer Guide</i>.',
        ),
    ]
    """
    The name of a header that you want CloudFront to forward to your origin. For more information, see <a href="http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html">Forwarding Custom Headers to Your Origin (Web Distributions Only)</a> in the <i>Amazon Amazon CloudFront Developer Guide</i>.
    """

    header_value: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="HeaderValue"),
        pydantic.Field(
            alias="HeaderValue",
            description="The value for the header that you specified in the <code>HeaderName</code> field.",
        ),
    ]
    """
    The value for the header that you specified in the <code>HeaderName</code> field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
