

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .media_type import MediaType
from .translations import Translations


class Media(UniversalBaseModel):
    caption: typing.Optional[str] = None
    id: typing.Optional[str] = None
    sequence: typing.Optional[int] = None
    translations: typing.Optional[Translations] = None
    type: typing.Optional[MediaType] = None
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
