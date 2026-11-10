

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubmitToolOutputsRunRequestToolOutputsItem(UniversalBaseModel):
    tool_call_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the tool call in the `required_action` object within the run object the output is being submitted for.
    """

    output: typing.Optional[str] = pydantic.Field(default=None)
    """
    The output of the tool call to be submitted to continue the run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
