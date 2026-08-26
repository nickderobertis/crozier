

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .completion_option import CompletionOption
from .completion_result_notification_op import CompletionResultNotificationOp
from .request_id import RequestId


class CompletionResultNotification(UniversalBaseModel):
    """
    Code completion result from language server.

        Attributes:
            completion_id: Request ID this responds to.
            prefix_length: Length of prefix to replace.
            options: Completion options to display.
    """

    completion_id: RequestId
    op: CompletionResultNotificationOp
    options: typing.List[CompletionOption]
    prefix_length: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
