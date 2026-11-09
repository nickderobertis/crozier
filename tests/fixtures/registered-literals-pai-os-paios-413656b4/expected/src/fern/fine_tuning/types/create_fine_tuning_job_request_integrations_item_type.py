

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateFineTuningJobRequestIntegrationsItemType(enum.StrEnum):
    WANDB = "wandb"

    def visit(self, wandb: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateFineTuningJobRequestIntegrationsItemType.WANDB:
            return wandb()
