

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file import File
from .translations import Translations


class Screenshot(UniversalBaseModel):
    caption: typing.Optional[str] = None
    file: typing.Optional[File] = None
    id: typing.Optional[str] = None
    translations: typing.Optional[Translations] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
