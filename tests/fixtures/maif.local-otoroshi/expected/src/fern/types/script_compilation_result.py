

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .script_compilation_error import ScriptCompilationError


class ScriptCompilationResult(UniversalBaseModel):
    """
    The result of the compilation of a Script
    """

    done: bool = pydantic.Field()
    """
    Is the task done or not
    """

    error: typing.Optional[ScriptCompilationError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
