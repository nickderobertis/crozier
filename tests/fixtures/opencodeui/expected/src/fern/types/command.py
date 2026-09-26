

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .command_source import CommandSource


class Command(UniversalBaseModel):
    name: str
    description: typing.Optional[str] = None
    agent: typing.Optional[str] = None
    model: typing.Optional[str] = None
    source: typing.Optional[CommandSource] = None
    template: str
    subtask: typing.Optional[bool] = None
    hints: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
