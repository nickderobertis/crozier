

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PromptMeta(UniversalBaseModel):
    name: str
    versions: typing.List[int]
    labels: typing.List[str]
    tags: typing.List[str]
    last_updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastUpdatedAt"), pydantic.Field(alias="lastUpdatedAt")
    ]
    last_config: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="lastConfig"), pydantic.Field(alias="lastConfig")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
