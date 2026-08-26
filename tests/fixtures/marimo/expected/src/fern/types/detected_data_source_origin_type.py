

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetectedDataSourceOriginType(enum.StrEnum):
    CONFIGURATION = "configuration"
    ENVIRONMENT = "environment"

    def visit(
        self, configuration: typing.Callable[[], T_Result], environment: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DetectedDataSourceOriginType.CONFIGURATION:
            return configuration()
        if self is DetectedDataSourceOriginType.ENVIRONMENT:
            return environment()
