

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RiskEvaluationRiskLevel(str, enum.Enum):
    """ """

    PENDING = "PENDING"
    NORMAL = "NORMAL"
    MODERATE = "MODERATE"
    HIGH = "HIGH"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        normal: typing.Callable[[], T_Result],
        moderate: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskEvaluationRiskLevel.PENDING:
            return pending()
        if self is RiskEvaluationRiskLevel.NORMAL:
            return normal()
        if self is RiskEvaluationRiskLevel.MODERATE:
            return moderate()
        if self is RiskEvaluationRiskLevel.HIGH:
            return high()
