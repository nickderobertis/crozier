

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ManualTaxType(str, enum.Enum):
    PAYGMANUAL = "PAYGMANUAL"
    ETPOMANUAL = "ETPOMANUAL"
    ETPRMANUAL = "ETPRMANUAL"
    SCHEDULE5MANUAL = "SCHEDULE5MANUAL"
    SCHEDULE5STSLMANUAL = "SCHEDULE5STSLMANUAL"

    def visit(
        self,
        paygmanual: typing.Callable[[], T_Result],
        etpomanual: typing.Callable[[], T_Result],
        etprmanual: typing.Callable[[], T_Result],
        schedule5manual: typing.Callable[[], T_Result],
        schedule5stslmanual: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ManualTaxType.PAYGMANUAL:
            return paygmanual()
        if self is ManualTaxType.ETPOMANUAL:
            return etpomanual()
        if self is ManualTaxType.ETPRMANUAL:
            return etprmanual()
        if self is ManualTaxType.SCHEDULE5MANUAL:
            return schedule5manual()
        if self is ManualTaxType.SCHEDULE5STSLMANUAL:
            return schedule5stslmanual()
