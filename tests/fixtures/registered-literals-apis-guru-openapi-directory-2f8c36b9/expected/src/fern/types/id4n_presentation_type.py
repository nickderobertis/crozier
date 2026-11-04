

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Id4NPresentationType(enum.StrEnum):
    """
    The type of ID
    """

    GUID = "GUID"
    ROUTING_COLLECTION = "ROUTING_COLLECTION"
    LOGISTIC_COLLECTION = "LOGISTIC_COLLECTION"
    LABELLED_COLLECTION = "LABELLED_COLLECTION"

    def visit(
        self,
        guid: typing.Callable[[], T_Result],
        routing_collection: typing.Callable[[], T_Result],
        logistic_collection: typing.Callable[[], T_Result],
        labelled_collection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Id4NPresentationType.GUID:
            return guid()
        if self is Id4NPresentationType.ROUTING_COLLECTION:
            return routing_collection()
        if self is Id4NPresentationType.LOGISTIC_COLLECTION:
            return logistic_collection()
        if self is Id4NPresentationType.LABELLED_COLLECTION:
            return labelled_collection()
