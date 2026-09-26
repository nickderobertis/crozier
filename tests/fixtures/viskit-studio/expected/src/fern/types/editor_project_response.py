

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EditorProjectResponse(UniversalBaseModel):
    checksum: str
    created_at: typing.Optional[str] = None
    document: typing.Dict[str, typing.Any]
    document_schema_version: int
    image_id: str
    project_id: str
    revision: int
    source_image_ref: typing.Optional[str] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
