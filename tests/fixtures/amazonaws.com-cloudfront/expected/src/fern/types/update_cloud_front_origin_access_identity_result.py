

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_cloud_front_origin_access_identity_result_cloud_front_origin_access_identity import (
    UpdateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity,
)


class UpdateCloudFrontOriginAccessIdentityResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    cloud_front_origin_access_identity: typing_extensions.Annotated[
        typing.Optional[UpdateCloudFrontOriginAccessIdentityResultCloudFrontOriginAccessIdentity],
        FieldMetadata(alias="CloudFrontOriginAccessIdentity"),
        pydantic.Field(alias="CloudFrontOriginAccessIdentity", description="The origin access identity's information."),
    ] = None
    """
    The origin access identity's information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
