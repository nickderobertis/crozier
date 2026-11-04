

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GuidCollectionType(enum.StrEnum):
    ROUTING_COLLECTION = "ROUTING_COLLECTION"
    LOGISTIC_COLLECTION = "LOGISTIC_COLLECTION"
    LABELLED_COLLECTION = "LABELLED_COLLECTION"

    def visit(
        self,
        routing_collection: typing.Callable[[], T_Result],
        logistic_collection: typing.Callable[[], T_Result],
        labelled_collection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GuidCollectionType.ROUTING_COLLECTION:
            return routing_collection()
        if self is GuidCollectionType.LOGISTIC_COLLECTION:
            return logistic_collection()
        if self is GuidCollectionType.LABELLED_COLLECTION:
            return labelled_collection()
