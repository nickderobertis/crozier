

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileMetaData(UniversalBaseModel):
    file_uuid: typing.Optional[str] = None
    location_id: typing.Optional[str] = None
    project_name: typing.Optional[str] = None
    node_name: typing.Optional[str] = None
    file_name: typing.Optional[str] = None
    file_id: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    last_modified: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    entity_tag: typing.Optional[str] = None
    is_directory: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
