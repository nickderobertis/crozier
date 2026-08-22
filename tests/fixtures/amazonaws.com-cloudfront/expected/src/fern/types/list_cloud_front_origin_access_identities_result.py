

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_cloud_front_origin_access_identities_result_cloud_front_origin_access_identity_list import (
    ListCloudFrontOriginAccessIdentitiesResultCloudFrontOriginAccessIdentityList,
)


class ListCloudFrontOriginAccessIdentitiesResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    cloud_front_origin_access_identity_list: typing_extensions.Annotated[
        typing.Optional[ListCloudFrontOriginAccessIdentitiesResultCloudFrontOriginAccessIdentityList],
        FieldMetadata(alias="CloudFrontOriginAccessIdentityList"),
        pydantic.Field(
            alias="CloudFrontOriginAccessIdentityList",
            description="The <code>CloudFrontOriginAccessIdentityList</code> type. ",
        ),
    ] = None
    """
    The <code>CloudFrontOriginAccessIdentityList</code> type. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
