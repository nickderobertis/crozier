

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceType(enum.StrEnum):
    COMPUTATIONAL = "computational"
    DYNAMIC = "dynamic"
    FRONTEND = "frontend"
    BACKEND = "backend"

    def visit(
        self,
        computational: typing.Callable[[], T_Result],
        dynamic: typing.Callable[[], T_Result],
        frontend: typing.Callable[[], T_Result],
        backend: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceType.COMPUTATIONAL:
            return computational()
        if self is ServiceType.DYNAMIC:
            return dynamic()
        if self is ServiceType.FRONTEND:
            return frontend()
        if self is ServiceType.BACKEND:
            return backend()
