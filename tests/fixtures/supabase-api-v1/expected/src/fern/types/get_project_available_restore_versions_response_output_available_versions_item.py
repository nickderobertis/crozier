

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_project_available_restore_versions_response_output_available_versions_item_postgres_engine import (
    GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemPostgresEngine,
)
from .get_project_available_restore_versions_response_output_available_versions_item_release_channel import (
    GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel,
)


class GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItem(UniversalBaseModel):
    version: str
    release_channel: GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemReleaseChannel
    postgres_engine: GetProjectAvailableRestoreVersionsResponseOutputAvailableVersionsItemPostgresEngine

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
