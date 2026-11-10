

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunStepDeltaStepDetailsToolCallsCodeOutputLogsObject(UniversalBaseModel):
    """
    Text output from the Code Interpreter tool call as part of a run step.
    """

    index: int = pydantic.Field()
    """
    The index of the output in the outputs array.
    """

    logs: typing.Optional[str] = pydantic.Field(default=None)
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
