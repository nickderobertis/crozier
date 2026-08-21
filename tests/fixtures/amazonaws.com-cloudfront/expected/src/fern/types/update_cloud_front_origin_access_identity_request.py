

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_cloud_front_origin_access_identity_request_cloud_front_origin_access_identity_config import (
    UpdateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig,
)


class UpdateCloudFrontOriginAccessIdentityRequest(UniversalBaseModel):
    """
    The request to update an origin access identity.
    """

    cloud_front_origin_access_identity_config: typing_extensions.Annotated[
        UpdateCloudFrontOriginAccessIdentityRequestCloudFrontOriginAccessIdentityConfig,
        FieldMetadata(alias="CloudFrontOriginAccessIdentityConfig"),
        pydantic.Field(
            alias="CloudFrontOriginAccessIdentityConfig", description="The identity's configuration information."
        ),
    ]
    """
    The identity's configuration information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
