

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_task_instance_new_state import UpdateTaskInstanceNewState


class UpdateTaskInstance(UniversalBaseModel):
    dry_run: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set, don't actually run this operation. The response will contain the task instance
    planned to be affected, but won't be modified in any way.
    """

    new_state: typing.Optional[UpdateTaskInstanceNewState] = pydantic.Field(default=None)
    """
    Expected new state.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
