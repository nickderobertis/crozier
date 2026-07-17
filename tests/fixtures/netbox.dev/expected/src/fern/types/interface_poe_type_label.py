

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterfacePoeTypeLabel(enum.StrEnum):
    EIGHT_HUNDRED_TWO3AF_TYPE1 = "802.3af (Type 1)"
    EIGHT_HUNDRED_TWO3AT_TYPE2 = "802.3at (Type 2)"
    EIGHT_HUNDRED_TWO3AZ_TYPE2 = "802.3az (Type 2)"
    EIGHT_HUNDRED_TWO3BT_TYPE3 = "802.3bt (Type 3)"
    EIGHT_HUNDRED_TWO3BT_TYPE4 = "802.3bt (Type 4)"
    PASSIVE24V2PAIR = "Passive 24V (2-pair)"
    PASSIVE24V4PAIR = "Passive 24V (4-pair)"
    PASSIVE48V2PAIR = "Passive 48V (2-pair)"
    PASSIVE48V4PAIR = "Passive 48V (4-pair)"

    def visit(
        self,
        eight_hundred_two3af_type1: typing.Callable[[], T_Result],
        eight_hundred_two3at_type2: typing.Callable[[], T_Result],
        eight_hundred_two3az_type2: typing.Callable[[], T_Result],
        eight_hundred_two3bt_type3: typing.Callable[[], T_Result],
        eight_hundred_two3bt_type4: typing.Callable[[], T_Result],
        passive24v2pair: typing.Callable[[], T_Result],
        passive24v4pair: typing.Callable[[], T_Result],
        passive48v2pair: typing.Callable[[], T_Result],
        passive48v4pair: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfacePoeTypeLabel.EIGHT_HUNDRED_TWO3AF_TYPE1:
            return eight_hundred_two3af_type1()
        if self is InterfacePoeTypeLabel.EIGHT_HUNDRED_TWO3AT_TYPE2:
            return eight_hundred_two3at_type2()
        if self is InterfacePoeTypeLabel.EIGHT_HUNDRED_TWO3AZ_TYPE2:
            return eight_hundred_two3az_type2()
        if self is InterfacePoeTypeLabel.EIGHT_HUNDRED_TWO3BT_TYPE3:
            return eight_hundred_two3bt_type3()
        if self is InterfacePoeTypeLabel.EIGHT_HUNDRED_TWO3BT_TYPE4:
            return eight_hundred_two3bt_type4()
        if self is InterfacePoeTypeLabel.PASSIVE24V2PAIR:
            return passive24v2pair()
        if self is InterfacePoeTypeLabel.PASSIVE24V4PAIR:
            return passive24v4pair()
        if self is InterfacePoeTypeLabel.PASSIVE48V2PAIR:
            return passive48v2pair()
        if self is InterfacePoeTypeLabel.PASSIVE48V4PAIR:
            return passive48v4pair()
