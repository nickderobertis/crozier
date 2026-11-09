

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlgorithmAdvisoryType(enum.StrEnum):
    ALGORITHM_ADVISORY = "algorithm_advisory"

    def visit(self, algorithm_advisory: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlgorithmAdvisoryType.ALGORITHM_ADVISORY:
            return algorithm_advisory()
