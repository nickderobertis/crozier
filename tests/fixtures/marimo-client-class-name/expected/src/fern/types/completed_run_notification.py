

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .completed_run_notification_op import CompletedRunNotificationOp


class CompletedRunNotification(UniversalBaseModel):
    """
    Run of submitted cells and descendants completed.

        Attributes:
            run_id: Correlation ID echoed from the command that triggered
                this completion. `None` for handlers that don't take a
                `run_id` (everything except `handle_execute_scratchpad`
                today). Consumers that want to wait for a specific command's
                completion filter on this field.
    """

    op: CompletedRunNotificationOp
    run_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
