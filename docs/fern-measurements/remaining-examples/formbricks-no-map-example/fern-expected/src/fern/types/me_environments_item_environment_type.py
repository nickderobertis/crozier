

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeEnvironmentsItemEnvironmentType(enum.StrEnum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"

    def visit(self, production: typing.Callable[[], T_Result], development: typing.Callable[[], T_Result]) -> T_Result:
        if self is MeEnvironmentsItemEnvironmentType.PRODUCTION:
            return production()
        if self is MeEnvironmentsItemEnvironmentType.DEVELOPMENT:
            return development()
