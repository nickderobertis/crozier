

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchRequestTypeItem(enum.StrEnum):
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
        if self is SearchRequestTypeItem.PUBLICATION:
            return publication()
        if self is SearchRequestTypeItem.DATASET:
            return dataset()
        if self is SearchRequestTypeItem.SOFTWARE:
            return software()
        if self is SearchRequestTypeItem.OTHER:
            return other()
