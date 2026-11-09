

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActivityType(enum.StrEnum):
    """
    Types of consent activities
    """

    UNKNOWN = "UNKNOWN"
    ITEM_CREATE = "ITEM_CREATE"
    ITEM_IMPORT = "ITEM_IMPORT"
    ITEM_UPDATE = "ITEM_UPDATE"
    ITEM_UNLINK = "ITEM_UNLINK"
    PORTAL_UNLINK = "PORTAL_UNLINK"
    PORTAL_ITEMS_DELETE = "PORTAL_ITEMS_DELETE"
    ITEM_REMOVE = "ITEM_REMOVE"
    INVARIANT_CHECKER_DELETION = "INVARIANT_CHECKER_DELETION"
    SCOPES_UPDATE = "SCOPES_UPDATE"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        item_create: typing.Callable[[], T_Result],
        item_import: typing.Callable[[], T_Result],
        item_update: typing.Callable[[], T_Result],
        item_unlink: typing.Callable[[], T_Result],
        portal_unlink: typing.Callable[[], T_Result],
        portal_items_delete: typing.Callable[[], T_Result],
        item_remove: typing.Callable[[], T_Result],
        invariant_checker_deletion: typing.Callable[[], T_Result],
        scopes_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActivityType.UNKNOWN:
            return unknown()
        if self is ActivityType.ITEM_CREATE:
            return item_create()
        if self is ActivityType.ITEM_IMPORT:
            return item_import()
        if self is ActivityType.ITEM_UPDATE:
            return item_update()
        if self is ActivityType.ITEM_UNLINK:
            return item_unlink()
        if self is ActivityType.PORTAL_UNLINK:
            return portal_unlink()
        if self is ActivityType.PORTAL_ITEMS_DELETE:
            return portal_items_delete()
        if self is ActivityType.ITEM_REMOVE:
            return item_remove()
        if self is ActivityType.INVARIANT_CHECKER_DELETION:
            return invariant_checker_deletion()
        if self is ActivityType.SCOPES_UPDATE:
            return scopes_update()
