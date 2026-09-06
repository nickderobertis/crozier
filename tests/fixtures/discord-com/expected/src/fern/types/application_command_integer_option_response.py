

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_command_option_integer_choice_response import ApplicationCommandOptionIntegerChoiceResponse
from .int53type import Int53Type


class ApplicationCommandIntegerOptionResponse(UniversalBaseModel):
    type: int
    name: str
    name_localized: typing.Optional[str] = None
    name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    description: str
    description_localized: typing.Optional[str] = None
    description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    required: typing.Optional[bool] = None
    autocomplete: typing.Optional[bool] = None
    choices: typing.Optional[typing.List[ApplicationCommandOptionIntegerChoiceResponse]] = None
    min_value: typing.Optional[Int53Type] = None
    max_value: typing.Optional[Int53Type] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
