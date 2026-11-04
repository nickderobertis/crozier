

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_sd_root_response_files_item_type import ListSdRootResponseFilesItemType


class ListSdRootResponseFilesItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    size: typing.Optional[int] = None
    type: typing.Optional[ListSdRootResponseFilesItemType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
