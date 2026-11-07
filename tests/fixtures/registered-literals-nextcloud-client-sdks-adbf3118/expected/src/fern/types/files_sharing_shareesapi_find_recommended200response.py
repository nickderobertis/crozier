

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_shareesapi_find_recommended200response_ocs import (
    FilesSharingShareesapiFindRecommended200ResponseOcs,
)


class FilesSharingShareesapiFindRecommended200Response(UniversalBaseModel):
    ocs: FilesSharingShareesapiFindRecommended200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
