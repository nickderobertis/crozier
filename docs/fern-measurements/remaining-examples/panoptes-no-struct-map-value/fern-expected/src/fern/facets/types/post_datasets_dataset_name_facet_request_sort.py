

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostDatasetsDatasetNameFacetRequestSort(enum.StrEnum):
    ASC = "asc"
    DESC = "desc"
    HITS = "hits"

    def visit(
        self,
        asc: typing.Callable[[], T_Result],
        desc: typing.Callable[[], T_Result],
        hits: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostDatasetsDatasetNameFacetRequestSort.ASC:
            return asc()
        if self is PostDatasetsDatasetNameFacetRequestSort.DESC:
            return desc()
        if self is PostDatasetsDatasetNameFacetRequestSort.HITS:
            return hits()
