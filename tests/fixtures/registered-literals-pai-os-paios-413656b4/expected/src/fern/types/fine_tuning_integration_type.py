

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FineTuningIntegrationType(enum.StrEnum):
    """
    The type of the integration being enabled for the fine-tuning job
    """

    WANDB = "wandb"

    def visit(self, wandb: typing.Callable[[], T_Result]) -> T_Result:
        if self is FineTuningIntegrationType.WANDB:
            return wandb()
