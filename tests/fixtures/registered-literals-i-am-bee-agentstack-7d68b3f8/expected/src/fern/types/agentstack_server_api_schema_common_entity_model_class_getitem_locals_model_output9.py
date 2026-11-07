

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_type import FileType


class AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9(UniversalBaseModel):
    id: str
    filename: str
    content_type: str
    file_size_bytes: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = None
    created_by: str
    file_type: typing.Optional[FileType] = None
    parent_file_id: typing.Optional[str] = None
    context_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
