

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_call_result_notification_op import FunctionCallResultNotificationOp
from .human_readable_status import HumanReadableStatus
from .request_id import RequestId


class FunctionCallResultNotification(UniversalBaseModel):
    """
    Result of a frontend-initiated function call.

        Attributes:
            function_call_id: ID matching the original request.
            return_value: Function return value as JSON.
            status: Human-readable success/failure status.
            found: Whether the requested function was located in the registry.
                False signals a transient registry desync, so the request is safe
                to retry. True means no retry will help: a non-ok status then
                reflects a failure unrelated to lookup, such as the function
                raising during execution or not being associated with a cell.
    """

    found: bool
    function_call_id: RequestId
    op: FunctionCallResultNotificationOp
    return_value: typing.Any
    status: HumanReadableStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
