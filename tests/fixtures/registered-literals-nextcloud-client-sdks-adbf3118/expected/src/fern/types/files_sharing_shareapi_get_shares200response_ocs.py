

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_share import FilesSharingShare
from .ocs_meta import OcsMeta


class FilesSharingShareapiGetShares200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: typing.List[FilesSharingShare]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
