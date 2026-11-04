

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateCollectionRequestType(enum.StrEnum):
    ROUTING_COLLECTION = "ROUTING_COLLECTION"
    LOGISTIC_COLLECTION = "LOGISTIC_COLLECTION"
    LABELLED_COLLECTION = "LABELLED_COLLECTION"

    def visit(
        self,
        routing_collection: typing.Callable[[], T_Result],
        logistic_collection: typing.Callable[[], T_Result],
        labelled_collection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateCollectionRequestType.ROUTING_COLLECTION:
            return routing_collection()
        if self is CreateCollectionRequestType.LOGISTIC_COLLECTION:
            return logistic_collection()
        if self is CreateCollectionRequestType.LABELLED_COLLECTION:
            return labelled_collection()
