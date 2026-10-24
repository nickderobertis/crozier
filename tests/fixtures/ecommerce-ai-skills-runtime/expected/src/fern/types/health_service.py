

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthService(enum.StrEnum):
    ECOMMERCE_AI_RUNTIME = "ecommerce-ai-runtime"

    def visit(self, ecommerce_ai_runtime: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthService.ECOMMERCE_AI_RUNTIME:
            return ecommerce_ai_runtime()
