

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_remote_get_share200response_ocs import FilesSharingRemoteGetShare200ResponseOcs


class FilesSharingRemoteGetShare200Response(UniversalBaseModel):
    ocs: FilesSharingRemoteGetShare200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
