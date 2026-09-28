

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ContactsRecordSubmitRequestOperation(enum.StrEnum):
    """
    Required unless cancelled is true
    """

    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    MERGE = "merge"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        merge: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactsRecordSubmitRequestOperation.CREATE:
            return create()
        if self is ContactsRecordSubmitRequestOperation.UPDATE:
            return update()
        if self is ContactsRecordSubmitRequestOperation.DELETE:
            return delete()
        if self is ContactsRecordSubmitRequestOperation.MERGE:
            return merge()
