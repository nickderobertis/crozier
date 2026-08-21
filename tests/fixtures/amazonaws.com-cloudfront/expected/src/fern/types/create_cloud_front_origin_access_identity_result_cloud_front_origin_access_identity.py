

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity_cloud_front_origin_access_identity_config import (
    CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig,
)


class CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity(UniversalBaseModel):
    """
    The origin access identity's information.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id", description="The ID for the origin access identity. For example: <code>E74FTE3AJFJ256A</code>. "
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
            description="The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3. ",
        ),
    ]
    """
    The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3. 
    """

    cloud_front_origin_access_identity_config: typing_extensions.Annotated[
        typing.Optional[
            CreateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentityCloudFrontOriginAccessIdentityConfig
        ],
        FieldMetadata(alias="CloudFrontOriginAccessIdentityConfig"),
        pydantic.Field(
            alias="CloudFrontOriginAccessIdentityConfig",
            description="The current configuration information for the identity. ",
        ),
    ] = None
    """
    The current configuration information for the identity. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
