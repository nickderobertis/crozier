

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_cloud_front_origin_access_identity_request_cloud_front_origin_access_identity_config import (
    CreateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig,
)


class CreateCloudFrontOriginAccessIdentityRequest(UniversalBaseModel):
    """
    The request to create a new origin access identity.
    """

    cloud_front_origin_access_identity_config: typing_extensions.Annotated[
        CreateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig,
        FieldMetadata(alias="CloudFrontOriginAccessIdentityConfig"),
        pydantic.Field(
            alias="CloudFrontOriginAccessIdentityConfig",
            description="The current configuration information for the identity.",
        ),
    ]
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
