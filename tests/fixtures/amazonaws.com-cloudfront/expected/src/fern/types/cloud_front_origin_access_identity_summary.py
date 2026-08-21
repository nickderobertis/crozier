

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CloudFrontOriginAccessIdentitySummary(UniversalBaseModel):
    """
    Summary of the information about a CloudFront origin access identity.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id", description="The ID for the origin access identity. For example: <code>E74FTE3AJFJ256A</code>."
        ),
    ]
    """
    The ID for the origin access identity. For example: <code>E74FTE3AJFJ256A</code>.
    """

    s3canonical_user_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="S3CanonicalUserId"),
        pydantic.Field(
            alias="S3CanonicalUserId",
            description="The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.",
        ),
    ]
    """
    The Amazon S3 canonical user ID for the origin access identity, which you use when giving the origin access identity read permission to an object in Amazon S3.
    """

    comment: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Comment"),
        pydantic.Field(
            alias="Comment",
            description="The comment for this origin access identity, as originally specified when created.",
        ),
    ]
    """
    The comment for this origin access identity, as originally specified when created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
