

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .location import Location
from .text import Text


class R2Locator(UniversalBaseModel):
    href: str
    kobo_span: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="koboSpan"), pydantic.Field(alias="koboSpan")
    ] = None
    locations: typing.Optional[Location] = None
    text: typing.Optional[Text] = None
    title: typing.Optional[str] = None
    type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
