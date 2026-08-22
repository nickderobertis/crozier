

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig(
    UniversalBaseModel
):
    """
    The current configuration information for the identity.
    """

    caller_reference: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallerReference"),
        pydantic.Field(
            alias="CallerReference",
            description="<p>A unique number that ensures the request can't be replayed.</p> <p>If the <code>CallerReference</code> is new (no matter the content of the <code>CloudFrontOriginAccessIdentityConfig</code> object), a new origin access identity is created.</p> <p>If the <code>CallerReference</code> is a value already sent in a previous identity request, and the content of the <code>CloudFrontOriginAccessIdentityConfig</code> is identical to the original request (ignoring white space), the response includes the same information returned to the original request. </p> <p>If the <code>CallerReference</code> is a value you already sent in a previous request to create an identity, but the content of the <code>CloudFrontOriginAccessIdentityConfig</code> is different from the original request, CloudFront returns a <code>CloudFrontOriginAccessIdentityAlreadyExists</code> error. </p>",
        ),
    ]
    """
    <p>A unique number that ensures the request can't be replayed.</p> <p>If the <code>CallerReference</code> is new (no matter the content of the <code>CloudFrontOriginAccessIdentityConfig</code> object), a new origin access identity is created.</p> <p>If the <code>CallerReference</code> is a value already sent in a previous identity request, and the content of the <code>CloudFrontOriginAccessIdentityConfig</code> is identical to the original request (ignoring white space), the response includes the same information returned to the original request. </p> <p>If the <code>CallerReference</code> is a value you already sent in a previous request to create an identity, but the content of the <code>CloudFrontOriginAccessIdentityConfig</code> is different from the original request, CloudFront returns a <code>CloudFrontOriginAccessIdentityAlreadyExists</code> error. </p>
    """

    comment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Comment"),
        pydantic.Field(
            alias="Comment", description="Any comments you want to include about the origin access identity. "
        ),
    ]
    """
    Any comments you want to include about the origin access identity. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
