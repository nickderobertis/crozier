

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NoteRevision(UniversalBaseModel):
    rev: int
    at: int = pydantic.Field()
    """
    Unix seconds
    """

    author: str
    title: str
    body_md: typing_extensions.Annotated[str, FieldMetadata(alias="bodyMd"), pydantic.Field(alias="bodyMd")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
