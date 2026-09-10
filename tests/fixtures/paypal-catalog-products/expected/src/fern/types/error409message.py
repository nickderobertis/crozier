

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error409Message(enum.StrEnum):
    THE_SERVER_HAS_DETECTED_A_CONFLICT_WHILE_PROCESSING_THIS_REQUEST = (
        "The server has detected a conflict while processing this request."
    )

    def visit(
        self, the_server_has_detected_a_conflict_while_processing_this_request: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is Error409Message.THE_SERVER_HAS_DETECTED_A_CONFLICT_WHILE_PROCESSING_THIS_REQUEST:
            return the_server_has_detected_a_conflict_while_processing_this_request()
