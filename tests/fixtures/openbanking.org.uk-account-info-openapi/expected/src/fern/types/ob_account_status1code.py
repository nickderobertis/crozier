

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObAccountStatus1Code(str, enum.Enum):
    """
    Specifies the status of account resource in code form.
    """

    DELETED = "Deleted"
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    PENDING = "Pending"
    PRO_FORMA = "ProForma"

    def visit(
        self,
        deleted: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        enabled: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        pro_forma: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObAccountStatus1Code.DELETED:
            return deleted()
        if self is ObAccountStatus1Code.DISABLED:
            return disabled()
        if self is ObAccountStatus1Code.ENABLED:
            return enabled()
        if self is ObAccountStatus1Code.PENDING:
            return pending()
        if self is ObAccountStatus1Code.PRO_FORMA:
            return pro_forma()
