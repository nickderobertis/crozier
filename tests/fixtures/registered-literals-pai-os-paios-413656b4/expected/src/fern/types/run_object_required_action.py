

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_object_required_action_submit_tool_outputs import RunObjectRequiredActionSubmitToolOutputs
from .run_object_required_action_type import RunObjectRequiredActionType


class RunObjectRequiredAction(UniversalBaseModel):
    """
    Details on the action required to continue the run. Will be `null` if no action is required.
    """

    type: RunObjectRequiredActionType = pydantic.Field()
    """
    For now, this is always `submit_tool_outputs`.
    """

    submit_tool_outputs: RunObjectRequiredActionSubmitToolOutputs = pydantic.Field()
    """
    Details on the tool outputs needed for this run to continue.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
