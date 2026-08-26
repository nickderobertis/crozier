

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_create_request_type import FileCreateRequestType


class FileCreateRequest(UniversalBaseModel):
    contents: typing.Optional[str] = None
    name: str
    path: str
    type: FileCreateRequestType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
