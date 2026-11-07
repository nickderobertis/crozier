

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeafColInfoType(enum.StrEnum):
    LEAF = "LEAF"
    LIST = "LIST"
    MAP = "MAP"
    SET = "SET"
    EMBEDDED = "EMBEDDED"
    DYNAMIC_OBJECT = "DYNAMIC_OBJECT"

    def visit(
        self,
        leaf: typing.Callable[[], T_Result],
        list_: typing.Callable[[], T_Result],
        map_: typing.Callable[[], T_Result],
        set_: typing.Callable[[], T_Result],
        embedded: typing.Callable[[], T_Result],
        dynamic_object: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LeafColInfoType.LEAF:
            return leaf()
        if self is LeafColInfoType.LIST:
            return list_()
        if self is LeafColInfoType.MAP:
            return map_()
        if self is LeafColInfoType.SET:
            return set_()
        if self is LeafColInfoType.EMBEDDED:
            return embedded()
        if self is LeafColInfoType.DYNAMIC_OBJECT:
            return dynamic_object()
