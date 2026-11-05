

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_v1player_releases_upload_response_data import PostApiV1PlayerReleasesUploadResponseData


class PostApiV1PlayerReleasesUploadResponse(UniversalBaseModel):
    data: typing.Optional[PostApiV1PlayerReleasesUploadResponseData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
