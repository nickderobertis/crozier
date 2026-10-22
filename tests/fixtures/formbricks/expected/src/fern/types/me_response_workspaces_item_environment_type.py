

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeResponseWorkspacesItemEnvironmentType(enum.StrEnum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"

    def visit(self, production: typing.Callable[[], T_Result], development: typing.Callable[[], T_Result]) -> T_Result:
        if self is MeResponseWorkspacesItemEnvironmentType.PRODUCTION:
            return production()
        if self is MeResponseWorkspacesItemEnvironmentType.DEVELOPMENT:
            return development()
