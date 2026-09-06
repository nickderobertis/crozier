

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .page_hash_known_dto_action import PageHashKnownDtoAction


class PageHashKnownDto(UniversalBaseModel):
    action: PageHashKnownDtoAction
    created: dt.datetime
    delete_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="deleteCount"), pydantic.Field(alias="deleteCount")
    ]
    hash: str
    last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ]
    match_count: typing_extensions.Annotated[int, FieldMetadata(alias="matchCount"), pydantic.Field(alias="matchCount")]
    size: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
