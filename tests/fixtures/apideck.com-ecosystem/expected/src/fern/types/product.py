

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file import File
from .translations import Translations


class Product(UniversalBaseModel):
    count: typing.Optional[int] = None
    description: typing.Optional[str] = None
    id: typing.Optional[str] = None
    logo: typing.Optional[File] = None
    name: str
    sequence: typing.Optional[int] = None
    slug: str
    translations: typing.Optional[Translations] = None
    visible: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
