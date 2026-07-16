

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoyaltyEventType(enum.StrEnum):
    """
    The type of the loyalty event.
    """

    ACCUMULATE_POINTS = "ACCUMULATE_POINTS"
    CREATE_REWARD = "CREATE_REWARD"
    REDEEM_REWARD = "REDEEM_REWARD"
    DELETE_REWARD = "DELETE_REWARD"
    ADJUST_POINTS = "ADJUST_POINTS"
    EXPIRE_POINTS = "EXPIRE_POINTS"
    OTHER = "OTHER"

    def visit(
        self,
        accumulate_points: typing.Callable[[], T_Result],
        create_reward: typing.Callable[[], T_Result],
        redeem_reward: typing.Callable[[], T_Result],
        delete_reward: typing.Callable[[], T_Result],
        adjust_points: typing.Callable[[], T_Result],
        expire_points: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoyaltyEventType.ACCUMULATE_POINTS:
            return accumulate_points()
        if self is LoyaltyEventType.CREATE_REWARD:
            return create_reward()
        if self is LoyaltyEventType.REDEEM_REWARD:
            return redeem_reward()
        if self is LoyaltyEventType.DELETE_REWARD:
            return delete_reward()
        if self is LoyaltyEventType.ADJUST_POINTS:
            return adjust_points()
        if self is LoyaltyEventType.EXPIRE_POINTS:
            return expire_points()
        if self is LoyaltyEventType.OTHER:
            return other()
