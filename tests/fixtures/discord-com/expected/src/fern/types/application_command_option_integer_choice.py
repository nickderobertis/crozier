

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .int53type import Int53Type


class ApplicationCommandOptionIntegerChoice(UniversalBaseModel):
    name: str
    name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    value: Int53Type

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
