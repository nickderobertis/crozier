

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_project_available_restore_versions_response_output_available_versions_item import (
    GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItem,
)


class GetProjectAvailableRestoreVersionsResponseOutput(UniversalBaseModel):
    available_versions: typing.List[GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
