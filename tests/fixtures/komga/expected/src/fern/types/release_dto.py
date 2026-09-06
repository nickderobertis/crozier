

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReleaseDto(UniversalBaseModel):
    description: str
    latest: bool
    pre_release: typing_extensions.Annotated[
        bool, FieldMetadata(alias="preRelease"), pydantic.Field(alias="preRelease")
    ]
    release_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="releaseDate"), pydantic.Field(alias="releaseDate")
    ]
    url: str
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
