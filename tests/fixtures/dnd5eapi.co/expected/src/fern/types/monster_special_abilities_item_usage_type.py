

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MonsterSpecialAbilitiesItemUsageType(str, enum.Enum):
    AT_WILL = "at will"
    PER_DAY = "per day"
    RECHARGE_AFTER_REST = "recharge after rest"
    RECHARGE_ON_ROLL = "recharge on roll"

    def visit(
        self,
        at_will: typing.Callable[[], T_Result],
        per_day: typing.Callable[[], T_Result],
        recharge_after_rest: typing.Callable[[], T_Result],
        recharge_on_roll: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonsterSpecialAbilitiesItemUsageType.AT_WILL:
            return at_will()
        if self is MonsterSpecialAbilitiesItemUsageType.PER_DAY:
            return per_day()
        if self is MonsterSpecialAbilitiesItemUsageType.RECHARGE_AFTER_REST:
            return recharge_after_rest()
        if self is MonsterSpecialAbilitiesItemUsageType.RECHARGE_ON_ROLL:
            return recharge_on_roll()
