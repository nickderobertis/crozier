

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_cloud_front_origin_access_identity_config_result_cloud_front_origin_access_identity_config import (
    GetCloudFrontOriginAccessIdentityConfigResultCloudFrontOriginAccessIdentityConfig,
)


class GetCloudFrontOriginAccessIdentityConfigResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    cloud_front_origin_access_identity_config: typing_extensions.Annotated[
        typing.Optional[GetCloudFrontOriginAccessIdentityConfigResultCloudFrontOriginAccessIdentityConfig],
        FieldMetadata(alias="CloudFrontOriginAccessIdentityConfig"),
        pydantic.Field(
            alias="CloudFrontOriginAccessIdentityConfig",
            description="The origin access identity's configuration information. ",
        ),
    ] = None
    """
    The origin access identity's configuration information. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
