

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdSeven(enum.StrEnum):
    ETL_PIPELINE_DEFAULT = "etl_pipeline_default"

    def visit(self, etl_pipeline_default: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdSeven.ETL_PIPELINE_DEFAULT:
            return etl_pipeline_default()
