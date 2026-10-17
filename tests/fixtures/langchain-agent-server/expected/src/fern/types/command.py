

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .command_goto import CommandGoto
from .command_resume import CommandResume
from .command_update import CommandUpdate


class Command(UniversalBaseModel):
    """
    The command to run.
    """

    update: typing.Optional[CommandUpdate] = pydantic.Field(default=None)
    """
    An update to the state.
    """

    resume: typing.Optional[CommandResume] = pydantic.Field(default=None)
    """
    A value to pass to an interrupted node.
    """

    goto: typing.Optional[CommandGoto] = pydantic.Field(default=None)
    """
    Name of the node(s) to navigate to next or node(s) to be executed with a provided input.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
