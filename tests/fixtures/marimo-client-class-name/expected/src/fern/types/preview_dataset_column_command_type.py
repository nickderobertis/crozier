

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreviewDatasetColumnCommandType(enum.StrEnum):
    PREVIEW_DATASET_COLUMN = "preview-dataset-column"

    def visit(self, preview_dataset_column: typing.Callable[[], T_Result]) -> T_Result:
        if self is PreviewDatasetColumnCommandType.PREVIEW_DATASET_COLUMN:
            return preview_dataset_column()
