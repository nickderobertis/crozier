

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetSignalResourceRequestStatus(str, enum.Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    def visit(self, success: typing.Callable[[], T_Result], failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSignalResourceRequestStatus.SUCCESS:
            return success()
        if self is GetSignalResourceRequestStatus.FAILURE:
            return failure()
