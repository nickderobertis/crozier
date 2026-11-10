

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunStepDetailsToolCallsCodeOutputLogsObject(UniversalBaseModel):
    """
    Text output from the Code Interpreter tool call as part of a run step.
    """

    logs: str = pydantic.Field()
    """
    The text output from the Code Interpreter tool call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
