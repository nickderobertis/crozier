

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OperatorType(str, enum.Enum):
    NORMALIZATION = "normalization"
    DBT = "dbt"
    WEBHOOK = "webhook"

    def visit(
        self,
        normalization: typing.Callable[[], T_Result],
        dbt: typing.Callable[[], T_Result],
        webhook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OperatorType.NORMALIZATION:
            return normalization()
        if self is OperatorType.DBT:
            return dbt()
        if self is OperatorType.WEBHOOK:
            return webhook()
