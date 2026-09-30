

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class Search1RequestTypeItem(enum.StrEnum):
    PUBLICATION = "publication"
    DATASET = "dataset"
    SOFTWARE = "software"
    OTHER = "other"

    def visit(
        self,
        publication: typing.Callable[[], T_Result],
        dataset: typing.Callable[[], T_Result],
        software: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Search1RequestTypeItem.PUBLICATION:
            return publication()
        if self is Search1RequestTypeItem.DATASET:
            return dataset()
        if self is Search1RequestTypeItem.SOFTWARE:
            return software()
        if self is Search1RequestTypeItem.OTHER:
            return other()
