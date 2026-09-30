

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .author_pid import AuthorPid


class Author(UniversalBaseModel):
    full_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fullName"), pydantic.Field(alias="fullName")
    ] = None
    name: typing.Optional[str] = None
    surname: typing.Optional[str] = None
    rank: typing.Optional[int] = None
    pid: typing.Optional[AuthorPid] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
