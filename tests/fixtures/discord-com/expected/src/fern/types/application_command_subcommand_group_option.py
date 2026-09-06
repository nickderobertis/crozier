

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_command_subcommand_option import ApplicationCommandSubcommandOption


class ApplicationCommandSubcommandGroupOption(UniversalBaseModel):
    type: int
    name: str
    name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    description: str
    description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    required: typing.Optional[bool] = None
    options: typing.Optional[typing.List[ApplicationCommandSubcommandOption]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
