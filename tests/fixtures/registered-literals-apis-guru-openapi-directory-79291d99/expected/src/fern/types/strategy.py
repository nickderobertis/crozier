

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Strategy(enum.StrEnum):
    """
    An instruction specifying what steps the new Identity Verification attempt should require the user to complete:


    `reset` - Restart the user at the beginning of the session, regardless of whether they successfully completed part of their previous session.

    `incomplete` - Start the new session at the step that the user failed in the previous session, skipping steps that have already been successfully completed.

    `infer` - If the most recent Identity Verification attempt associated with the given `client_user_id` has a status of `failed` or `expired`, retry using the `incomplete` strategy. Otherwise, use the `reset` strategy.

    `custom` - Start the new session with a custom configuration, specified by the value of the `steps` field

    Note:

    The `incomplete` strategy cannot be applied if the session's failing step is `screening` or `risk_check`.

    The `infer` strategy cannot be applied if the session's status is still `active`
    """

    RESET = "reset"
    INCOMPLETE = "incomplete"
    INFER = "infer"
    CUSTOM = "custom"

    def visit(
        self,
        reset: typing.Callable[[], T_Result],
        incomplete: typing.Callable[[], T_Result],
        infer: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Strategy.RESET:
            return reset()
        if self is Strategy.INCOMPLETE:
            return incomplete()
        if self is Strategy.INFER:
            return infer()
        if self is Strategy.CUSTOM:
            return custom()
