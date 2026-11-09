

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tag import Tag
from .tag_map_entity import TagMapEntity


class TagMap(UniversalBaseModel):
    entity: TagMapEntity
    target: str
    refresh_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="refreshDate"), pydantic.Field(alias="refreshDate")
    ]
    tags: typing.List[Tag]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
