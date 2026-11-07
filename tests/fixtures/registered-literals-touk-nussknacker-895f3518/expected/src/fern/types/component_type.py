

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ComponentType(enum.StrEnum):
    SOURCE = "source"
    SINK = "sink"
    SERVICE = "service"
    CUSTOM = "custom"
    FRAGMENT = "fragment"
    BUILTIN = "builtin"

    def visit(
        self,
        source: typing.Callable[[], T_Result],
        sink: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        fragment: typing.Callable[[], T_Result],
        builtin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ComponentType.SOURCE:
            return source()
        if self is ComponentType.SINK:
            return sink()
        if self is ComponentType.SERVICE:
            return service()
        if self is ComponentType.CUSTOM:
            return custom()
        if self is ComponentType.FRAGMENT:
            return fragment()
        if self is ComponentType.BUILTIN:
            return builtin()
