

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NestedFhrpGroupProtocol(str, enum.Enum):
    VRRP2 = "vrrp2"
    VRRP3 = "vrrp3"
    CARP = "carp"
    CLUSTERXL = "clusterxl"
    HSRP = "hsrp"
    GLBP = "glbp"
    OTHER = "other"

    def visit(
        self,
        vrrp2: typing.Callable[[], T_Result],
        vrrp3: typing.Callable[[], T_Result],
        carp: typing.Callable[[], T_Result],
        clusterxl: typing.Callable[[], T_Result],
        hsrp: typing.Callable[[], T_Result],
        glbp: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NestedFhrpGroupProtocol.VRRP2:
            return vrrp2()
        if self is NestedFhrpGroupProtocol.VRRP3:
            return vrrp3()
        if self is NestedFhrpGroupProtocol.CARP:
            return carp()
        if self is NestedFhrpGroupProtocol.CLUSTERXL:
            return clusterxl()
        if self is NestedFhrpGroupProtocol.HSRP:
            return hsrp()
        if self is NestedFhrpGroupProtocol.GLBP:
            return glbp()
        if self is NestedFhrpGroupProtocol.OTHER:
            return other()
