

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputSelectedAddonsItemVariantIdSeven(enum.StrEnum):
    ETL_PIPELINE_DEFAULT = "etl_pipeline_default"

    def visit(self, etl_pipeline_default: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputSelectedAddonsItemVariantIdSeven.ETL_PIPELINE_DEFAULT:
            return etl_pipeline_default()
