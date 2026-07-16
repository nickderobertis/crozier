

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfacePoeTypeValue(str, enum.Enum):
    TYPE1IEEE8023AF = "type1-ieee802.3af"
    TYPE2IEEE8023AT = "type2-ieee802.3at"
    TYPE2IEEE8023AZ = "type2-ieee802.3az"
    TYPE3IEEE8023BT = "type3-ieee802.3bt"
    TYPE4IEEE8023BT = "type4-ieee802.3bt"
    PASSIVE24V2PAIR = "passive-24v-2pair"
    PASSIVE24V4PAIR = "passive-24v-4pair"
    PASSIVE48V2PAIR = "passive-48v-2pair"
    PASSIVE48V4PAIR = "passive-48v-4pair"

    def visit(
        self,
        type1ieee8023af: typing.Callable[[], T_Result],
        type2ieee8023at: typing.Callable[[], T_Result],
        type2ieee8023az: typing.Callable[[], T_Result],
        type3ieee8023bt: typing.Callable[[], T_Result],
        type4ieee8023bt: typing.Callable[[], T_Result],
        passive24v2pair: typing.Callable[[], T_Result],
        passive24v4pair: typing.Callable[[], T_Result],
        passive48v2pair: typing.Callable[[], T_Result],
        passive48v4pair: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfacePoeTypeValue.TYPE1IEEE8023AF:
            return type1ieee8023af()
        if self is InterfacePoeTypeValue.TYPE2IEEE8023AT:
            return type2ieee8023at()
        if self is InterfacePoeTypeValue.TYPE2IEEE8023AZ:
            return type2ieee8023az()
        if self is InterfacePoeTypeValue.TYPE3IEEE8023BT:
            return type3ieee8023bt()
        if self is InterfacePoeTypeValue.TYPE4IEEE8023BT:
            return type4ieee8023bt()
        if self is InterfacePoeTypeValue.PASSIVE24V2PAIR:
            return passive24v2pair()
        if self is InterfacePoeTypeValue.PASSIVE24V4PAIR:
            return passive24v4pair()
        if self is InterfacePoeTypeValue.PASSIVE48V2PAIR:
            return passive48v2pair()
        if self is InterfacePoeTypeValue.PASSIVE48V4PAIR:
            return passive48v4pair()
