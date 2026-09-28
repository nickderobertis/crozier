

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ManageOrgDataRequestOperation(enum.StrEnum):
    """
    Operation to perform on the cluster data
    """

    LIST = "list"
    GET = "get"
    DELETE = "delete"
    DELETE_ALL = "deleteAll"
    SCAN = "scan"
    PROGRESS = "progress"
    SEARCH = "search"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        get: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        delete_all: typing.Callable[[], T_Result],
        scan: typing.Callable[[], T_Result],
        progress: typing.Callable[[], T_Result],
        search: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ManageOrgDataRequestOperation.LIST:
            return list_()
        if self is ManageOrgDataRequestOperation.GET:
            return get()
        if self is ManageOrgDataRequestOperation.DELETE:
            return delete()
        if self is ManageOrgDataRequestOperation.DELETE_ALL:
            return delete_all()
        if self is ManageOrgDataRequestOperation.SCAN:
            return scan()
        if self is ManageOrgDataRequestOperation.PROGRESS:
            return progress()
        if self is ManageOrgDataRequestOperation.SEARCH:
            return search()
