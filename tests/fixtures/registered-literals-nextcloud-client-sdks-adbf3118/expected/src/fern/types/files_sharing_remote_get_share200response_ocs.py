

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_remote_share import FilesSharingRemoteShare
from .ocs_meta import OcsMeta


class FilesSharingRemoteGetShare200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: FilesSharingRemoteShare

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
