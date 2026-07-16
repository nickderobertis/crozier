

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LeaveLineCalculationType(str, enum.Enum):
    """
    Calculation type for leave line for Opening Balance on Employee
    """

    NOCALCULATIONREQUIRED = "NOCALCULATIONREQUIRED"
    FIXEDAMOUNTEACHPERIOD = "FIXEDAMOUNTEACHPERIOD"
    ENTERRATEINPAYTEMPLATE = "ENTERRATEINPAYTEMPLATE"
    BASEDONORDINARYEARNINGS = "BASEDONORDINARYEARNINGS"
    EMPTY = ""

    def visit(
        self,
        nocalculationrequired: typing.Callable[[], T_Result],
        fixedamounteachperiod: typing.Callable[[], T_Result],
        enterrateinpaytemplate: typing.Callable[[], T_Result],
        basedonordinaryearnings: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LeaveLineCalculationType.NOCALCULATIONREQUIRED:
            return nocalculationrequired()
        if self is LeaveLineCalculationType.FIXEDAMOUNTEACHPERIOD:
            return fixedamounteachperiod()
        if self is LeaveLineCalculationType.ENTERRATEINPAYTEMPLATE:
            return enterrateinpaytemplate()
        if self is LeaveLineCalculationType.BASEDONORDINARYEARNINGS:
            return basedonordinaryearnings()
        if self is LeaveLineCalculationType.EMPTY:
            return empty()
