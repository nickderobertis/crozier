

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_sd_root_response_files_item import ListSdRootResponseFilesItem


class ListSdRootResponse(UniversalBaseModel):
    path: typing.Optional[str] = None
    files: typing.Optional[typing.List[ListSdRootResponseFilesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
