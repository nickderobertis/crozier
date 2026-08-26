

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DatasetsNotificationOp(enum.StrEnum):
    DATASETS = "datasets"

    def visit(self, datasets: typing.Callable[[], T_Result]) -> T_Result:
        if self is DatasetsNotificationOp.DATASETS:
            return datasets()
