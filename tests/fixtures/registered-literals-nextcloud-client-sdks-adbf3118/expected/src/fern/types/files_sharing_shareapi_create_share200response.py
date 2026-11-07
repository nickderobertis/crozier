

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_shareapi_create_share200response_ocs import FilesSharingShareapiCreateShare200ResponseOcs


class FilesSharingShareapiCreateShare200Response(UniversalBaseModel):
    ocs: FilesSharingShareapiCreateShare200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
