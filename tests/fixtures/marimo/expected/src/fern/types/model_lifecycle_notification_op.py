

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelLifecycleNotificationOp(enum.StrEnum):
    MODEL_LIFECYCLE = "model-lifecycle"

    def visit(self, model_lifecycle: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelLifecycleNotificationOp.MODEL_LIFECYCLE:
            return model_lifecycle()
