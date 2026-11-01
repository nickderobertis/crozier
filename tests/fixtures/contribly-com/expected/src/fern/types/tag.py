

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tag_set import TagSet


class Tag(UniversalBaseModel):
    colour: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional HTML hexcode colour
    """

    id: str
    name: str
    tag_set: typing_extensions.Annotated[
        typing.Optional[TagSet], FieldMetadata(alias="tagSet"), pydantic.Field(alias="tagSet")
    ] = None
    url_words: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="urlWords"), pydantic.Field(alias="urlWords")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
