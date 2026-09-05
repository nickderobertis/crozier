

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApplicationCommandOptionNumberChoiceResponse(UniversalBaseModel):
    name: str
    name_localized: typing.Optional[str] = None
    name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
