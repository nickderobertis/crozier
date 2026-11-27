

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppCollaboratorType(enum.StrEnum):
    APP = "APP"

    def visit(self, app: typing.Callable[[], T_Result]) -> T_Result:
        if self is AppCollaboratorType.APP:
            return app()
