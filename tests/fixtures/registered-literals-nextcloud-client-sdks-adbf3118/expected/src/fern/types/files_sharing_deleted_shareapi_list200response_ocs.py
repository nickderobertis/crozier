

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_deleted_share import FilesSharingDeletedShare
from .ocs_meta import OcsMeta


class FilesSharingDeletedShareapiList200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: typing.List[FilesSharingDeletedShare]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
